# STACK ADT:
# PUSH
# POP
# empty
# top

class Stack:
    def __init__(self):
        self._items = []

    def empty(self):
        return len(self._items) == 0

    # allow the index error 
    def top(self):
        if self.empty():
            raise IndexError("top() on an empty stack")
        return self._items[-1]

    def push(self, item):
        self._items.append(item)

    # also allow the index error
    def pop(self):
        if self.empty():
            raise IndexError("pop() on an empty stack")
        return self._items.pop()