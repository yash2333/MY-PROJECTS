"""Descriptive statistics implemented with the Python standard library."""
from math import sqrt
from statistics import median


def mean(values: list[float]) -> float:
    """Return arithmetic mean; reject an empty collection."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def describe(values: list[float]) -> dict[str, float]:
    """Return count, min, max, mean, median, and population standard deviation."""
    if not values:
        raise ValueError("values must not be empty")
    if any(not isinstance(x, (int, float)) for x in values):
        raise TypeError("all values must be numeric")
    average = mean(values)
    variance = sum((x - average) ** 2 for x in values) / len(values)
    return {
        "count": len(values),
        "min": min(values),
        "max": max(values),
        "mean": average,
        "median": median(values),
        "population_stddev": sqrt(variance),
    }
