from text_handler_and_statistic import *


def main():
    unprocessed_text = load_text('Роман «Анна Каренина».txt')
    tokenized_text = clean_text(unprocessed_text)
    processed_text = remove_stopwords(tokenized_text)

    counter = count_words(processed_text)
    freq = display_top_words(counter)

    print(f'Наиболее часто встречающиеся слова:\n{dict(freq)}')


if __name__ == "__main__":
    main()
