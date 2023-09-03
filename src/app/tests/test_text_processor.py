from src.app.utils.text_processor import process_article, most_common_words

def test_process_article():
    text = "This is a test sentence with symbols: @#*! and a number 123."
    words = process_article(text)
    assert words == ["This", "is", "a", "test", "sentence", "with", "symbols", "and", "a", "number", "123"]

def test_most_common_words():
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    common_words = most_common_words(words, 2)
    assert common_words == ["apple", "banana"]
