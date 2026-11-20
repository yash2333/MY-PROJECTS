"""Small, dependency-free text processing helpers."""
from collections import Counter
import re
import unicodedata


def normalize_whitespace(value: str) -> str:
    """Collapse consecutive whitespace and trim the result."""
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    return " ".join(value.split())


def word_count(value: str) -> int:
    """Count Unicode-aware word-like tokens."""
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    return len(re.findall(r"\b[\w']+\b", value, flags=re.UNICODE))


def is_palindrome(value: str) -> bool:
    """Return whether letters and digits read identically in reverse."""
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    normalized = "".join(
        ch.casefold() for ch in unicodedata.normalize("NFKC", value)
        if ch.isalnum()
    )
    return normalized == normalized[::-1]


def character_frequency(value: str) -> dict[str, int]:
    """Return counts of non-whitespace characters, preserving case."""
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    return dict(Counter(ch for ch in value if not ch.isspace()))
