import re
import unicodedata
from collections import Counter

def normalize_whitespace(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError('value must be a string')
    return ' '.join(value.split())

def word_count(value: str) -> int:
    if not isinstance(value, str):
        raise TypeError('value must be a string')
    return len(re.findall(r"\b[\w']+\b", value))

def is_palindrome(value: str) -> bool:
    text = ''.join(c.casefold() for c in unicodedata.normalize('NFKC', value) if c.isalnum())
    return text == text[::-1]

def character_frequency(value: str) -> dict[str, int]:
    return dict(Counter(c for c in value if not c.isspace()))
