class LinkedListNode:
    def __init__(self, key, val, next_node=None):
        self.key = key
        self.val = val
        self.next = next_node

    def to_list(self):
        L = [f"{self.key}:{self.val}"]
        curr_node = self.next
        while curr_node is not None:
            L.append(f"{curr_node.key}:{curr_node.val}")
            curr_node = curr_node.next
        return L

class HashMap:
    def __init__(self):
        """
        Size is the number of buckets
        load_factor if the ratio of elements:numbers
            s.t. number of elements/number of bucks <= lf
        Buckets are the linked_lists where elems are stored
            Separate chaining
        """
        self.size = 32
        self.load_factor = 1.5
        # every bucket in the array is a sorted linked list
        self.buckets = [None] * self.size
        self.elems = 0

    def rehash(self):
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [None] * self.size

        # rehash all values
        for node in old_buckets:
            if node is not None:
                self.put(node.key, node.val)
                curr_node = node.next
                while curr_node is not None:
                    self.put(node.key, node.val)
                    curr_node = curr_node.next

    def put(self, key, value):
        # need to rehash to decrease collision probability
        if self.elems / self.size > self.load_factor:
            self.rehash()

        index = hash(key) % self.size  # fast hash for integers
        if self.buckets[index] is None:
            self.buckets[index] = LinkedListNode(key, value)
            self.elems += 1
        else:
            curr_node = self.buckets[index]
            if curr_node.key == key:
                curr_node.val = value
            else:
                while curr_node.next is not None:
                    if curr_node.next.key == key:
                        curr_node.next.val = value
                        return
                    curr_node = curr_node.next
                curr_node.next = LinkedListNode(key, value)
                self.elems += 1

    def remove(self, key: int) -> None:
        index = hash(key) % self.size
        if self.buckets[index] is None:
            return

        curr_node = self.buckets[index]
        if curr_node.val == key:
            self.buckets[index] = curr_node.next # can be None
            self.elems -= 1 
        else:
            while curr_node.next is not None and curr_node.next.key != key:
                curr_node = curr_node.next
            if curr_node.next is not None and curr_node.next.key == key:
                curr_node.next = curr_node.next.next
                self.elems -= 1

    def get(self, key: int) -> bool:
        index = hash(key) % self.size
        curr_node = self.buckets[index]
        while curr_node is not None:
            if curr_node.key == key:
                return curr_node.val
            curr_node = curr_node.next
        return -1

    def __str__(self):
        L = []
        for node in self.buckets:
            if node is not None:
                L.extend(node.to_list())
        return str(L)