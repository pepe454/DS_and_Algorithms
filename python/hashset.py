class LinkedListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def  to_list(self):
        L = [self.val]
        curr_node = self.next
        while curr_node is not None:
            L.append(curr_node.val)
            curr_node = curr_node.next
        return L

    def __str__(self):
        list_str = f"{self.val}"
        curr_node = self.next
        while curr_node is not None:
            list_str += f"->{curr_node.val}"
            curr_node = curr_node.next
        return list_str

class HashSet:
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
        self.buckets = [None] * self.size # every bucket in the array is a sorted linked list
        self.elems = 0
    
    def rehash(self):
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [None] * self.size
        
        # rehash all values
        for node in old_buckets:
            if node is not None:
                self.add(node.val)
                curr_node = node.next
                while curr_node is not None:
                    self.add(curr_node.val)
                    curr_node = curr_node.next

    def add(self, key):
        index = hash(key) % self.size # fast hash for integers
        
        if self.buckets[index] is not None:
            curr_node = self.buckets[index]
            if curr_node.val == key:
                return
            while curr_node.next is not None and curr_node.next.val != key:
                curr_node = curr_node.next
            if curr_node.next is not None and curr_node.next.val == key:
                return
            curr_node.next = LinkedListNode(key)
            self.elems += 1 
        
        else:
            self.buckets[index] = LinkedListNode(key)
            self.elems += 1

        if float(self.elems) / float(self.size) > self.load_factor: # need to rehash to decrease collision probability
            self.rehash()
        

    def remove(self, key: int) -> None:
        index = hash(key) % self.size

        if self.buckets[index] is not None:
            curr_node = self.buckets[index]
            if curr_node.val == key:
                self.buckets[index] = curr_node.next # can be None
                self.elems -= 1
            else:
                while curr_node.next is not None and curr_node.next.val != key:
                    curr_node = curr_node.next

                if curr_node.next is not None and curr_node.next.val == key:
                    curr_node.next = curr_node.next.next
                    self.elems -= 1
        

    def contains(self, key: int) -> bool:
        index = hash(key) % self.size
        curr_node = self.buckets[index]
        while curr_node is not None:
            if curr_node.val == key:
                return True
            curr_node = curr_node.next
        return False

    def __str__(self):
        L = []
        for node in self.buckets:
            if node is not None:
                L.extend(node.to_list())
        return str(L)