import re
from collections import Counter
from typing import List

def process_article(text: str) -> List[str]:
    words = text.split()
    cleaned_words = [re.sub(r'\W+', '', word) for word in words]
    non_empty_words = list(filter(None, cleaned_words))
    return non_empty_words

def most_common_words(words: List[str], n: int = 10) -> List[str]:
    counter = Counter(words)
    return [word for word, _ in counter.most_common(n)]
