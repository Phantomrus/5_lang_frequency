import collections
import re

def load_data(filepath):
    with open(filepath, 'r') as text_file:
        text_file= text_file.read()
    return text_file

def get_most_frequent_words(text):
    words = re.findall(r'\w+', text.lower())
    freq_words = []  
    print('\nTen most frequent words:')
    for pair in collections.Counter(words).most_common(10):
        freq_words.append([pair[0], pair[1]]) # Получаем 10 самых часто встречающихся слов и количество их появлений и добавляем в массив 
    return freq_words


if __name__ == '__main__':
    file_path = input("Enter the path to the file: ")
    text = load_data(file_path)
    ten_freq_words = get_most_frequent_words(text)
    for element in ten_freq_words:
        print(element[0], element[1])
