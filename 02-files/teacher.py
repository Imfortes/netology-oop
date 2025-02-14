def merge_files(file_names):
    sorted_file_data = sorted(((name, len(open(name, encoding='utf-8').readlines())) for name in file_names), key=lambda x: x[1])

    with open('result.txt', 'w', encoding='utf-8') as result_file:
        for file_name, line_count in sorted_file_data:
            file_content = open(file_name, encoding='utf-8').read()
            result_file.write(f'Имя файла: {file_name}\\n')
            result_file.write(f'Количество строк: {line_count}\\n')
            result_file.write(file_content + '\\n\\')
