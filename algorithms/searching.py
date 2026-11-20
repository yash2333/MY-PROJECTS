def linear_search(items: list, target) -> int:
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1

def binary_search(items: list, target) -> int:
    low, high = 0, len(items) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
