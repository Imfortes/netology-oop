import os
from collections import Counter

class Book:
    def __init__(self):
        pass

    def read_txt(self, file_path):
        recipes = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                recipe = None
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    if '|' not in line and not line.isdigit():
                        recipe = line
                        recipes[recipe] = []
                    else:
                        parts = line.split('|')
                        if len(parts) == 3:  
                            ingridients_name, quantity, measure = parts
                            recipes[recipe].append({
                                'ingridients_name': ingridients_name.strip(),
                                'quantity': int(quantity.strip()),
                                'measure': measure.strip()
                            })
                        
            return recipes
        except FileNotFoundError:
            print(f'Ошибка: файл {file_path} не найден')

    def get_shop_list_by_dishes(self, dishes, person_count):
        shop_list = {} 
        dishes_counter = Counter(dishes)
        
        for recipe in cook_book:
            if recipe in dishes:
                for ingredient in cook_book[recipe]: 
                    name = ingredient['ingridients_name']
                    quantity = ingredient['quantity'] * person_count * dishes_counter[recipe]
                    measure = ingredient['measure']

                    if name in shop_list:
                        shop_list[name]['quantity'] += quantity
                    else:
                        shop_list[name] = {
                            'measure': measure,
                            'quantity': quantity
                        }
        return sorted(shop_list.items()) 

class File:
    @staticmethod
    def files_concat(file_paths, output_file):
        files_info = []
        
        for file_path in file_paths:
            try:
                with open(file_path, 'r', encoding="utf-8") as file:
                    lines = file.readlines()
                    file_name = os.path.basename(file_path)
                    files_info.append({
                        'name': file_name,
                        'line_count': len(lines),
                        'content': ''.join(lines)
                    })
                    
            except FileNotFoundError:
                print(f'File "{file_path}" not found.') 
                continue
            
        files_info.sort(key=lambda x: x['line_count'])
            
        try:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                for file_info in files_info:
                    outfile.write(f'{file_info["name"]}\n')
                    outfile.write(f'{file_info["line_count"]}\n')
                    outfile.write(f'{file_info["content"]}\n')
        except Exception as e:
            print(f'Ошибка записи {e}')
            
    @staticmethod
    def merge_files(file_names):
        # try:
        #     sorted_file_data = sorted(((name, len(open(name, encoding='utf-8').readlines())) for name in file_names), key=lambda x: x[1])
        # except:
        #     print('Произошла ошибка')
        try:
            sorted_file_data = sorted(
                ((name, sum(1 for _ in open(name, encoding='utf-8'))) for name in file_names),
                key=lambda x: x[1]
            )
            return sorted_file_data
        except FileNotFoundError as e:
            print(f'Ошибка: файл не найден - {e}')
        except Exception as e:
            print(f'Произошла ошибка: {e}')

        with open('./02-files/result_2.txt', 'w', encoding='utf-8') as result_file:
            for file_name, line_count in sorted_file_data:
                file_content = open(file_name, encoding='utf-8').read()
                result_file.write(f'Имя файла: {file_name}\n')
                result_file.write(f'Количество строк: {line_count}\n')
                result_file.write(file_content + '\n')



if __name__ == '__main__':
    book = Book()

    cook_book = book.read_txt('./02-files/recipes.txt')
    print(f'Книга рецептов: {cook_book}')
    
    person_count = 4
    shop_list = book.get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Фахитос', 'Фахитос', 'Омлет', 'Омлет', 'Картошка'], person_count)
    print(f'Список покупок на {person_count} персон: {shop_list}')
    
    print()
    
    
    input_files = ['./02-files/1.txt', './02-files/2.txt', './02-files/3.txt']
    output_file = './02-files/result.txt'
    files_result = File.files_concat(input_files, output_file)
    
    files_result_2 = File.merge_files(['./02-files/1.txt', './02-files/2.txt', './02-files/3.txt'])
    