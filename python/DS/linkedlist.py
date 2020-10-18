'''
Doubly Linked List ADT
insert front
insert back
remove front
remove back
get front
get back
'''

class Node:
    def __init__(self, item, prev=None, next_node=None):
        self.item = item
        self.prev = prev
        self.next_node = next_node 

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def peek_front(self):
        if self._head is None:
            raise IndexError("peek on an empty list")
        return self._head.item

    def peek_back(self):
        if self._tail is None:
            raise IndexError("peek on an empty list")
        return self._tail.item

    def insert_front(self, item):
        new_node = Node(item)
        # in a LL with 1 node, the head and tail are the same
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            old_head = self._head
            old_head.prev = new_node
            new_node.next_node = old_head
            self._head = new_node
        self._length += 1

    def insert_back(self, item):
        # in a LL with 1 node, the head and tail are the same
        if self._tail is None:
            self.insert_front(item)
        else:
            new_node = Node(item)
            old_tail = self._tail
            old_tail.next_node = new_node
            new_node.prev = old_tail
            self._tail = new_node
            self._length += 1

    def remove_front(self):
        if self._head is None:
            raise IndexError("remove on an empty linked list")
        old_head = self._head
        front_item = old_head.item
        new_head = old_head.next_node
        self._head = new_head
        self._length -= 1

        # there was only one element in the ll
        # now it is empty again
        if self._head is None:
            self._tail = None
        else:
            self._head.prev = None
        return front_item

    def remove_back(self):
        if self._tail is None:
            raise IndexError("remove on an empty linked list")
        
        # there is only one element in the LL
        if self._length == 1:
            return self.remove_front()

        # remove the tail and replace with its previous node
        old_tail = self._tail
        back_item = old_tail.item
        new_tail = old_tail.prev
        self._tail = new_tail
        self._tail.next_node = None
        self._length -= 1
        return back_item

    def __repr__(self):
        items = []
        curr_node = self._head
        while curr_node is not None:
            items.append(repr(curr_node.item))
            curr_node = curr_node.next_node
        return "->".join(items)

    def __len__(self):
        return self._length
