""" main.py """

# ------------------------------ #
#                                #
#  version 0.0.1                 #
#                                #
#  Aleksiej Ostrowski, 2023      #
#                                #
#  bstu-hackathon.ru             #
#  KONWPALTO                     #
#                                #
# ------------------------------ #

# Constants
MAGIC_SIMILARITY_VALUE = 10003
THRESHOLD = 0.5
CORPUS_PATH = "data/corpus.bin"
FIT_MODEL = "data/answers.json"

# Standard library imports
from math import sqrt, ceil
import json

# Third-party imports
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from pymorphy2 import MorphAnalyzer
from gensim.models import KeyedVectors


def get_word_pos(word):
    """
    Get the part of speech (POS) tag for a given word.

    Parameters:
    word (str): The word for which POS tag is required.

    Returns:
    str: The POS tag of the word.
    """
    morph = MorphAnalyzer()
    parsed_word = morph.parse(word)[0]
    return parsed_word.tag.POS


def calculate_similarity(word1, word2, corpus):
    """
    Calculate the similarity between two words using a given corpus.

    Parameters:
    word1, word2 (str): The words for which similarity is to be calculated.
    corpus: The corpus to use for similarity calculation.

    Returns:
    float: The similarity score between the two words.
    """
    if word1 in corpus.key_to_index and word2 in corpus.key_to_index:
        return corpus.similarity(word1, word2)
    else:
        return MAGIC_SIMILARITY_VALUE


def pymorphy_normalization(tokens):
    """
    Normalize a list of tokens using pymorphy2 MorphAnalyzer.

    Args:
    tokens (list of str): A list of word tokens to be normalized.

    Returns:
    list of str: A list of normalized tokens.
    """
    morph = MorphAnalyzer()
    normalized_tokens = [morph.parse(token)[0].normal_form for token in tokens]
    return normalized_tokens


def preprocess_text(text):
    """
    Preprocess a given text for NLP tasks by tokenizing and normalizing the words.

    This function tokenizes the text into words, normalizes these words, and
    appends their parts of speech to them. Filters out words shorter than 3 characters.

    Args:
    text (str): The text to be preprocessed.

    Returns:
    list of str: A list of preprocessed tokens with their parts of speech.
    """

    tokens = word_tokenize(text, language="russian")
    normalized_tokens = pymorphy_normalization(tokens)
    return [
        f"{token}_{get_word_pos(token)}"
        for token in normalized_tokens
        if len(token) > 2
    ]


def modified_tanh(x):
    """
    Apply a modified hyperbolic tangent function to an input.

    This function modifies the standard hyperbolic tangent function by scaling its output.

    Args:
    x (float): A numerical input to the tanh function.

    Returns:
    float: The result of the modified tanh function applied to x.
    """
    return 13.13 * np.tanh(x)


def similarity(sentence1, sentence2, corpus):
    """
    Calculate the similarity between two sentences based on the Jaccard Index.

    The function preprocesses the sentences, calculates word similarities, and
    then computes the Jaccard Index based on the unique words that surpass
    a defined similarity threshold. It applies a modified tanh function to the
    Jaccard Index for the final similarity score.

    Parameters:
    sentence1 (str): The first sentence to compare.
    sentence2 (str): The second sentence to compare.
    corpus (list or set): The corpus of words used for similarity calculation.

    Returns:
    int: A rounded similarity score between the two sentences.
    """

    # print(sentence1, sentence2)

    words1 = preprocess_text(sentence1)
    words2 = preprocess_text(sentence2)

    # print(words1)
    # print(words2)

    like = []
    for word1 in words1:
        for word2 in words2:
            res = 1.0
            if word1 != word2:
                res = calculate_similarity(word1, word2, corpus)
                if res == MAGIC_SIMILARITY_VALUE:
                    continue
            if res > THRESHOLD:
                like.extend([word1, word2])

    unique_words1 = set(words1)
    unique_words2 = set(words2)

    intersection = len(set(like))
    union = len(unique_words1.union(unique_words2))

    jaccard_index = intersection / union if union else 0.0

    # print(jaccard_index)

    return round(modified_tanh(jaccard_index))


def fit(fit_model):
    """
    Reads a JSON file and extracts key-value pairs.

    Args:
    fit_model (str): Path to the JSON file to be read.

    Returns:
    dict: A dictionary with ids as keys and corresponding answers as values.
    """
    res = {}
    with open(fit_model, "r") as file:
        try:
            data = json.load(file)
            for item in data:
                res[item["id"]] = item["answers"]
        except json.JSONDecodeError:
            print(f"Error: The file {fit_model} is not a valid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return res


def process_json_file(file_name, fit_model, corpus):
    """
    Processes a JSON file, updates it based on a model and a corpus.

    Args:
    file_name (str): Path to the JSON file to be processed.
    fit_model (dict): A model containing key-value pairs for processing.
    corpus (list): A list representing the corpus used for similarity comparison.

    Returns:
    None: The function updates the file in-place and does not return anything.
    """
    try:
        with open(file_name, "r") as file:
            data = json.load(file)

        if data["question_id"] in fit_model:
            items = fit_model[data["question_id"]]
            answer = data["answer"]

            data["evaluation"] = max([similarity(el, answer, corpus) for el in items])

            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)

    except json.JSONDecodeError:
        print(f"Error: The file {file_name} is not a valid JSON.")
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    corpus = KeyedVectors.load_word2vec_format(CORPUS_PATH, binary=True)
    nltk.download("punkt")

    model = fit(FIT_MODEL)

    import argparse

    parser = argparse.ArgumentParser(description="Process a JSON file.")
    parser.add_argument(
        "-input",
        "--input_file",
        required=True,
        type=str,
        help="Path to the JSON file to be processed",
    )
    args = parser.parse_args()

    process_json_file(args.input_file, model, corpus)
