import os
from collections import defaultdict

class Book:
    def __init__(self):
        self.cook_book = defaultdict(list)
    
    def _parse_recipe(self, lines):
        recipe_name = lines[0].strip()
        ingredient_count = int(lines[1].strip())
        ingredients = [dict(zip(('ingridients_name', 'quantity', 'measure'), 
                                map(str.strip, line.split('|')))) for line in lines[2:2+ingredient_count]]
        return recipe_name, ingredients

    def read_txt(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                recipes = [list(g) for k, g in itertools.groupby(content.split('\n'), bool) if k]
                for recipe in recipes:
                    name, ingrs = self._parse_recipe(recipe)
                    self.cook_book[name] = [{'ingridients_name': i['ingridients_name'], 
                                             'quantity': int(i['quantity']), 
                                             'measure': i['measure']} for i in ingrs]
        except FileNotFoundError:
            print(f'Ошибка: файл {file_path} не найден')
        except Exception as e:
            print(f'Ошибка чтения файла: {e}')

    def get_shop_list_by_dishes(self, dishes, person_count):
        if not isinstance(dishes, list) or not all(isinstance(dish, str) for dish in dishes):
            raise ValueError("dishes должен быть списком строк")
        if not isinstance(person_count, int) or person_count <= 0:
            raise ValueError("person_count должен быть положительным целым числом")

        shop_list = defaultdict(lambda: {'quantity': 0, 'measure': ''})
        for dish in dishes:
            if dish not in self.cook_book:
                print(f"Рецепт {dish} не найден")
                continue
            for ingredient in self.cook_book[dish]:
                name = ingredient['ingridients_name']
                quantity = ingredient['quantity'] * person_count 
                measure = ingredient['measure']
                shop_list[name]['quantity'] += quantity
                shop_list[name]['measure'] = measure
        return dict(shop_list)

class File:
    @staticmethod
    def files_concat(*file_list):
        if not all(isinstance(f, str) and os.path.isfile(f) for f in file_list):
            raise ValueError("Все элементы file_list должны быть существующими файлами")

        try:
            with open('./02-experiment/result.txt', 'w', encoding='utf-8') as outfile:
                files_info = []
                for f in file_list:
                    with open(f, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        files_info.append((os.path.basename(f), len(content), content))
                
                for file_name, length, content in sorted(files_info, key=lambda x: x[1]):
                    outfile.write(f"{file_name}\n{length}\n{content}\n\n")
        except Exception as e:
            raise IOError(f"Ошибка при объединении файлов: {e}")

if __name__ == '__main__':
    book = Book()
    book.read_txt('./02-experiment/recipes.txt')
    print(f'Книга рецептов: {dict(book.cook_book)}')
    
    person_count = 4
    try:
        shop_list = book.get_shop_list_by_dishes(['Омлет', 'Фахитос'], person_count)
        print(f'Список покупок на {person_count} персон: {dict(shop_list)}')
    except ValueError as ve:
        print(f"Ошибка параметров: {ve}")
    
    print()
    
    try:
        File.files_concat('./02-experiment/1.txt', './02-experiment/2.txt', './02-experiment/3.txt')
    except ValueError as ve:
        print(f"Ошибка параметров: {ve}")
    except IOError as ie:
        print(f"Ошибка файловой операции: {ie}")