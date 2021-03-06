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
    print('%s most frequent words:' % count_of_words)
    for word, count in words.most_common(count_of_words):
        print(word, count)

if __name__ == '__main__':
    count_of_words = int(input("Enter the number of the most frequent words which you want to output: "))
    file_path = input("Enter the path to the file: ")
    text = load_data(file_path)
    words = get_words(text)
    print_ten_freq_words(words, count_of_words)
