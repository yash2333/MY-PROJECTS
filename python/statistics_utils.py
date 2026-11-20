from math import sqrt
from statistics import median

def describe(values: list[float]) -> dict[str, float]:
    if not values:
        raise ValueError('values must not be empty')
    if any(not isinstance(x, (int, float)) for x in values):
        raise TypeError('all values must be numeric')
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return {'count': len(values), 'min': min(values), 'max': max(values), 'mean': avg, 'median': median(values), 'population_stddev': sqrt(variance)}
