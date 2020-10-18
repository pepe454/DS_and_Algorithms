'''
QUEUE ADT
 enqueue: push to front
 dequeue: remove from back
'''

from DS import LinkedList

class Queue:
    def __init__(self, input_restricted=False, output_restricted=False):
        self._items = LinkedList()
        # if true, user may ONLY enqueue at the front
        self._input_restricted = input_restricted
        # if true, user may only dequeue/pop from the back
        self._output_restricted = output_restricted

    def empty(self):
        return len(self) == 0

    # add to front of the queue
    def enqueue(self, item):
        self._items.insert_front(item)

    # pop off the back
    def dequeue(self):
        if self.empty():
            raise IndexError("Dequeue on an empty Queue")
        return self._items.remove_back()

    def enqueue_back(self, item):
        if self._input_restricted:
            raise Exception("insert on input restricted queue")
        self._items.insert_back(item)

    def dequeue_front(self):
        if self._output_restricted:
            raise Exception("remove on output restricted queue")
        if self.empty():
            raise IndexError("Dequeue on an empty Queue")
        return self._items.remove_front()

    def peek_front(self):
        return self._items.peek_front()

    def peek_back(self):
        return self._items.peek_back()

    def __repr__(self):
        return repr(self._items)

    def __len__(self):
        return len(self._items)