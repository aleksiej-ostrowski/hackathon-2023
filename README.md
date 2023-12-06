# hackathon-2023

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
    
    
## :: ПОДГОТОВКА ::    
    
Для питона должны быть загружены следующие ПАКЕТЫ:    
    
1) ```python
python3 -m pip install -r requirements.txt    
```
    
2) /data/corpus.bin это файл model.bin из архива    
[ruwikiruscorpora_upos_cbow_300](https://rusvectores.org/en/models/#ruwikiruscorpora_upos_cbow_300_10_2021)
    
## :: ПОРЯДОК РАБОТЫ ::    
   
```python
python3 main.py --input_file example_input.json    
```
    
# Пример ВХОДНОГО файла example_input.json для тестирования с точностью до запятой:    

```json    
{        
    "student_id": 1,        
    "question_id": "B-DS-15-5",        
    "answer": "Тематическое моделирование - это метод анализа текстовых данных, который позволяет выделить скрытые темы и понимать, какие слова и фразы связаны с этими темами. "        
}        
```

# Пример ВЫХОДНОГО файла example_input.json:    

```json
{    
    "student_id": 1,    
    "question_id": "B-DS-15-5",    
    "answer": "\u0422\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043c\u043e\u0434\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 - \u044d\u0442\u043e \u043c\u0435\u0442\u043e\u0434 \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0445
    "evaluation": 10    
}    
```
    
@aleksiej_ostrowski
