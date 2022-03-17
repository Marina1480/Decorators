import os
import datetime
import json

def logger_with_path(path):
    def logger(old_function):
        def new_function(*args, **kwargs):
            res_d = {}
            result = old_function(*args, **kwargs)
            res_d['date-time'] = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
            res_d['name'] = old_function.__name__
            res_d['arguments'] = args, kwargs
            res_d['result'] = result
            print(res_d)
            with open('logs_new.json', 'w', encoding='utf-8') as file:
                json.dump(res_d, file)
            return result
        return new_function
    return logger


@logger_with_path(path=os.path.join(os.getcwd(), 'logs_new.json'))
def cook_book_read(file):
    with open(file, 'r', encoding="utf-8") as file:
        cook_book = {}
        for line in file:
            ingredients = []
            dish_name = line.strip()
            ingredients_number = int(file.readline().strip())
            for ingredient in range(ingredients_number):
                name, count, measure = file.readline().strip().split('|')
                ingredients.append({'ingredient_name': name.strip(), 'quantity': int(count),
                                    'measure': measure.strip()})
            file.readline()
            cook_book[dish_name] = ingredients
    print(cook_book)
    return cook_book

p = cook_book_read("recipes.txt")

