"""Classic searching algorithms."""


def linear_search(items: list, target) -> int:
    """Return the first matching index, or -1; O(n) time, O(1) space."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def binary_search(items: list, target) -> int:
    """Search a sorted sequence; O(log n) time, O(1) space.

    The input must be sorted in ascending order.
    """
    left, right = 0, len(items) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if items[middle] == target:
            return middle
        if items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
