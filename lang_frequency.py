import collections
import re

def load_data(filepath):
    with open(filepath, 'r') as text_file:
        text_file= text_file.read()
    return text_file

def get_words(text):
    words = re.findall(r'\w+', text.lower())
    return collections.Counter(words)

def print_ten_freq_words(words, count_of_words):
    print('Ten most frequent words:')
    for pair in words.most_common(count_of_words):
        print(pair[0], pair[1]) # Выводим самые часто встречающиеся слова (количество содержится в переменной count_of_words) и количество их появлений.

if __name__ == '__main__':
    count_of_words = 10 # Количество самых часто встречаемых слов, которое мы хотим вывести на экран.
    file_path = input("Enter the path to the file: ")
    text = load_data(file_path)
    words = get_words(text)
    print_ten_freq_words(words, count_of_words)
