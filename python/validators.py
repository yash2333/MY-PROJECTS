import re

def is_valid_email(value: str) -> bool:
    return isinstance(value, str) and len(value) <= 254 and bool(re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', value))

def is_indian_pin_code(value: str) -> bool:
    return isinstance(value, str) and bool(re.fullmatch(r'[1-9]\d{5}', value))

def is_strong_password(value: str) -> bool:
    return isinstance(value, str) and len(value) >= 8 and any(c.islower() for c in value) and any(c.isupper() for c in value) and any(c.isdigit() for c in value) and any(not c.isalnum() for c in value)
