import json



# получаем json
# добираемся до нужного уровня вложености
# генератором списков получаем описание новостей - список
# приводим все к нижнему регистру и строке
# разбиваем строку на список слов
# фильтрация слов по условию если короче какого то количества симвоов например 3
# import Counter и считаем каунтер 
# делаем вывод и если надо либо возвращаем список, либо проходим в списке и ф строкой возвращаем слово и количество повтороений

try:
    with open('./03-json_xml/news.json', 'r', encoding='utf-8') as f:
        template = json.load(f)
        news_item = template['rss']['channel']['items']
        description = [news['description'] for news in news_item]

        all_text = ' '.join(description)
        words = all_text.split()
        
        filtered_words = [word for word in words if len(word) > 3]
        
        word_count = {}
        for word in filtered_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        top_10_word = []
        temp_word_count = word_count.copy()
        
        for _ in range(10):
            max_word = None
            max_count = 0
            
            for word, count in temp_word_count.items():
                if count > max_count:
                    max_word = word
                    max_count = count
                    
            if max_word is not None:
                top_10_word.append(max_word)
                del(temp_word_count[max_word])
                
        print(top_10_word)


except FileNotFoundError:
    print('Error: The file was not found.')

except json.JSONDecodeError:
    print('Error: The file is not a valid JSON.')

except Exception as e:
    print(f'An unexpected error occurred: {e}')