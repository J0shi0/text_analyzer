from collections import Counter

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')


def load_text(file_name: str):
    # Открытие файла в контекстном менеджере
    with open(file_name, 'r', encoding='utf8') as f:
        return f.read()


def clean_text(text):
    # Токенизация текста
    tokens = word_tokenize(text, language='russian')
    # Приведение к нижнему регистру и удаление знаков препинания
    cleaned_tokens = [token.lower() for token in tokens if token.isalnum()]
    return cleaned_tokens


def remove_stopwords(tokens):
    stop_words = set(stopwords.words('russian'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens


def count_words(tokens):
    return Counter(tokens)


def display_top_words(counted_tokens: Counter, num_top=10):
    return counted_tokens.most_common(num_top)
