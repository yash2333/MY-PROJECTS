def merge_sort(items: list) -> list:
    if len(items) < 2:
        return items.copy()
    mid = len(items) // 2
    left, right = merge_sort(items[:mid]), merge_sort(items[mid:])
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

def quick_sort(items: list) -> list:
    if len(items) < 2:
        return items.copy()
    pivot = items[len(items) // 2]
    return quick_sort([x for x in items if x < pivot]) + [x for x in items if x == pivot] + quick_sort([x for x in items if x > pivot])
