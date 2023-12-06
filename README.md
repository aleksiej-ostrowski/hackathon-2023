# hackathon-2023

```
           .,,.    
        ,;;'';;    
       , ;;'`;;    
      / . . . .`\    
     / .`\. . . . \    
    ; . . . .`\/` .;    
   | . . . . . `\ / |    
   |. . . . . . |;  ;    
   | .KONWPALTO/;  /    
   |. . . . . / / ,|    
    \ .POVTAS` /,(    
     \ . . . . .),\    
      \ . 2023. /, `.    
       \ . . . / )  .'    
        `._ _.'  ,  ;     
          `.`.`-' .'     
            `-...-'    
``` 
    
## :: ПОДГОТОВКА ::    
    
Для питона должны быть загружены следующие ПАКЕТЫ:    
    
```bash
python3 -m pip install -r requirements.txt    
```
    
2) `/data/corpus.bin` это файл `model.bin` из архива    
[ruwikiruscorpora_upos_cbow_300](https://rusvectores.org/en/models/#ruwikiruscorpora_upos_cbow_300_10_2021)
    
## :: ПОРЯДОК РАБОТЫ ::    
   
```bash
python3 main.py --input_file example_input.json    
```
    
### Пример ВХОДНОГО файла `example_input.json` для тестирования:    

```json    
{        
    "student_id": 1,        
    "question_id": "B-DS-15-5",        
    "answer": "Тематическое моделирование - это метод анализа текстовых данных, который позволяет выделить скрытые темы и понимать, какие слова и фразы связаны с этими темами. "        
}        
```

### Пример ВЫХОДНОГО файла `example_input.json`:    

```json
{    
    "student_id": 1,    
    "question_id": "B-DS-15-5",    
    "answer": "Тематическое моделирование - это метод анализа текстовых данных, который позволяет выделить скрытые темы и понимать, какие слова и фразы связаны с этими темами. ",
    "evaluation": 10    
}    
```

[@aleksiej_ostrowski](https://t.me/aleksiej_ostrowski)
