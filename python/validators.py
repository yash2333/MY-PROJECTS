"""Lightweight validators for common user input."""
import re


def is_valid_email(value: str) -> bool:
    """Perform practical structural email validation (not mailbox verification)."""
    if not isinstance(value, str) or len(value) > 254:
        return False
    return bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", value))


def is_indian_pin_code(value: str) -> bool:
    """Check the six-digit Indian postal PIN structure."""
    return isinstance(value, str) and bool(re.fullmatch(r"[1-9]\d{5}", value))


def is_strong_password(value: str) -> bool:
    """Require 8+ chars with upper, lower, digit, and symbol."""
    if not isinstance(value, str) or len(value) < 8:
        return False
    return (
        any(c.islower() for c in value)
        and any(c.isupper() for c in value)
        and any(c.isdigit() for c in value)
        and any(not c.isalnum() for c in value)
    )
