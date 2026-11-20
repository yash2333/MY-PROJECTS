"""Sorting algorithms that return new lists."""


def merge_sort(items: list) -> list:
    """Stable O(n log n) sort using O(n) auxiliary space."""
    if len(items) < 2:
        return items.copy()
    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


def quick_sort(items: list) -> list:
    """Readable recursive quick sort; average O(n log n), worst O(n²)."""
    if len(items) < 2:
        return items.copy()
    pivot = items[len(items) // 2]
    lower = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    upper = [x for x in items if x > pivot]
    return quick_sort(lower) + equal + quick_sort(upper)
