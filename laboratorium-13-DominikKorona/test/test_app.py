from app import hello
from app import extract_sentiment
from app import text_contain_word
from app import bubblesort
import pytest


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


testdata1 = ["I think today will be a great day"]


@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):
    sentiment = extract_sentiment(sample)

    assert sentiment > 0


testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
]


@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):
    assert text_contain_word(word, sample) == expected_output


# I
# def test_bubblesort():
#     unsored_lst = [4, 3, 6, 2, 1]
#     got = bubblesort(unsored_lst)
#     want = [4, 3, 6, 2, 1]
#     assert got[0] == want

# II
test_data3 = [([4, 3, 6, 2, 1], [1, 2, 3, 4, 6]),
              ([9, 8, 7, 5, 4], [4, 5, 7, 8, 9])]


@pytest.mark.parametrize('lst, expected_output', test_data3)
def test_bubblesort(lst, expected_output):
    assert bubblesort(lst)[0] == expected_output
