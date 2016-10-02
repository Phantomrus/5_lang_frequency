import collections
import re

def load_data(filepath):
    text_file = open(filepath, 'r').read()
    return text_file

def get_most_frequent_words(text):
    count_dict = collections.Counter() # Создаем объект типа Counter
    words = re.findall(r'\w+', text.lower())
    
    for word in words: # Для каждого слова файла
        count_dict[word] += 1 # Обновляем количество появления этого слова
    
    print('Ten most frequent words:')
    for pair in count_dict.most_common(10):
        print(pair[0], pair[1]) # Выводим 10 самых часто встречающихся слов и количество их появлений


if __name__ == '__main__':
    file_path = input("Enter the path to the file: ")
    text = load_data(file_path)
    get_most_frequent_words(text)