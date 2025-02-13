import os

class Book:
    def __init__(self):
        pass

    def read_txt(self, file_path):
        recipes = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                recipe = None
                for line in lines:
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
        for recipe in cook_book:
            if recipe in dishes:
                for ingredient in cook_book[recipe]: 
                    name = ingredient['ingridients_name']
                    quantity = ingredient['quantity'] * person_count 
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
    def files_concat(*file_list):
        files_sorted_by_length = {}
        try:
            with open('./02-files/result.txt', 'w', encoding='utf-8') as outfile:
                for f in file_list:
                    with open(f, 'r', encoding='utf-8') as infile:
                        file_name = os.path.basename(f)
                        file_content = infile.read()
                        file_length = len(file_content)
                        files_sorted_by_length[file_name] = file_length
                        
                        outfile.write(file_name + '\n')
                        outfile.write(str(file_length) + '\n')
                        outfile.write(file_content + '\n\n')
                        
            print(sorted(files_sorted_by_length.values()))
            print(files_sorted_by_length)
        except Exception as e:
            raise FileExistsError(f'Error: {e}')


if __name__ == '__main__':
    book = Book()

    cook_book = book.read_txt('./02-files/recipes.txt')
    print(f'Книга рецептов: {cook_book}')
    
    person_count = 4
    shop_list = book.get_shop_list_by_dishes(['Омлет', 'Фахитос'], person_count)
    print(f'Список покупок на {person_count} персон: {shop_list}')
    
    print()
    
    files = File()
    files_result = files.files_concat('./02-files/1.txt', './02-files/2.txt', './02-files/3.txt')
    print(files_result)