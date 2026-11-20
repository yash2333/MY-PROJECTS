"""Simple stack and queue containers."""


class Stack:
    """Last-in, first-out container."""
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def __len__(self):
        return len(self._items)


class Queue:
    """First-in, first-out container with O(1) dequeue."""
    def __init__(self):
        from collections import deque
        self._items = deque()

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def __len__(self):
        return len(self._items)
