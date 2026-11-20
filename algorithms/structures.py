from collections import deque

class Stack:
    def __init__(self):
        self._items = []
    def push(self, value):
        self._items.append(value)
    def pop(self):
        if not self._items:
            raise IndexError('pop from empty stack')
        return self._items.pop()
    def __len__(self):
        return len(self._items)

class Queue:
    def __init__(self):
        self._items = deque()
    def enqueue(self, value):
        self._items.append(value)
    def dequeue(self):
        if not self._items:
            raise IndexError('dequeue from empty queue')
        return self._items.popleft()
    def __len__(self):
        return len(self._items)
