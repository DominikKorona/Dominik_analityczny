from textblob import TextBlob
from typing import List, Tuple

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    return word in text


def bubblesort(a: list) -> Tuple[List, int]:
    n = len(a)
    zmiana = True
    counter = 0
    a_copy = a.copy()
    while n > 1 and zmiana:
        zmiana = False
        for i in range(1, n):
            if a_copy[i - 1] > a_copy[i]:
                a_copy[i - 1], a_copy[i] = a_copy[i], a_copy[i - 1]
                zmiana = True
            counter += 1
        n -= 1
    return a_copy, counter
