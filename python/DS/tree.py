'''
All kinds of binary trees welcome here
Naive BST
AVL tree
Red-Black tree
Splay tree

BST ADT:
search(key)
insert(key, value)
delete(key)
traverse_inorder()
traverse_preorder()
traverse_postorder()
'''

class BSTNode:
    def __init__(self, key, value, left_child=None, right_child=None):
        self.key = key
        self.value = value
        # left_child must be a BSTNode or None
        self.left = left_child
        # right_child must be a BSTNode or None
        self.right = right_child

    # return true if key is present in the tree
    def search(self, key):
        if self.key > key:
            if self.left is None:
                raise KeyError
            return self.left.search(key)
        elif self.key < key:
            if self.right is None:
                raise KeyError
            return self.right.search(key)
        return self.value

    # leftmost
    def minimum(self):
        if self.left is None:
            return self
        return self.left.minimum()

    # rightmost 
    def maximum(self):
        if self.right is None:
            return self
        return self.right.maximum()

    def insert(self, key, value):
        # traverse left 
        if self.key > key:
            if self.left is None:
                self.left = BSTNode(key,value)
            else:
                self.left.insert(key, value)
        # traverse right
        elif self.key < key:
            if self.right is None:
                self.right = BSTNode(key,value)
            else:
                self.right.insert(key, value)

        # update value: keys are identical 
        else:
            self.value = value

    # harvest internals of another bst into this node
    def swap(self, other):
        self.key, other.key = other.key, self.key
        self.value, other.value = other.value, self.value

    def remove(self, key):
        # the current node must be removed
        if self.key == key:
            # in the 3rd case, when left and right are both None
            # this will simply return None which is desired
            if self.right is None: 
                return self.left
            if self.left is None:
                return self.right

            # both children are present, we must swap root with
            # its inorder successor, then remove root from right subtree            
            else:
                replacement = self.right.minimum()
                self.swap(replacement)
                self.right = self.right.remove(key)

        # remove from left subtree
        elif self.key > key and self.left is not None:
            self.left = self.left.remove(key)
        # remove from the right subtree
        elif self.key < key and self.right is not None:
            self.right = self.right.remove(key)
        # key is not in the tree
        else:
            raise KeyError('delete on a non-existent key!')
        return self

    def __repr__(self):
        return f"[({self.key} : {self.value} -> {repr(self.left)} {repr(self.right)}]"

class BST:
    def __init__(self):
        self._root = None

    def insert(self, key, value):
        if self._root is None:
            self._root = BSTNode(key, value)
        else:
            self._root.insert(key, value)

    def remove(self, key):
        if self._root is None:
            raise KeyError("remove on an empty tree!")
        self._root = self._root.remove(key)

    def search(self, key):
        if self._root is None:
            raise KeyError("search on an empty tree!")
        return self._root.search(key)

    def __repr__(self):
        return repr(self._root)
