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
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

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

    def insert(self, node):
        try:
            a,b = node.key,node.value
        except AttributeError:
            raise ValueError("trying to insert a non-node into the tree") 

        if self.key > node.key:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        elif self.key < node.key:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
        else:
            self.value = node.value

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
        return f"[<{self.key}, {self.value}> : {repr(self.left)}, {repr(self.right)}]"

class BST:
    node = BSTNode
    def __init__(self):
        self._root = None

    def insert(self, key, value):
        if self._root is None:
            self._root = self.node(key, value)
        else:
            self._root.insert(self.node(key, value))

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


class AVLNode(BSTNode):
    def __init__(self, key, value):
        super().__init__(key, value)
        self.update_height()

    def update_height(self):
        left_height, right_height = 0, 0
        if self.left is not None: 
            left_height = self.left.height
        if self.right is not None: 
            right_height = self.right.height
        self.height = 1 + max(left_height, right_height)
        return self.height

    def balance(self):
        balance = 0
        if self.left is not None:
            balance += self.left.height
        if self.right is not None:
            balance -= self.right.height
        return balance 
    
    def insert(self, node):
        try:
            a,b = node.key,node.value
        except AttributeError:
            raise ValueError("trying to insert a non-node into the tree") 

        if self.key > node.key:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
            self.update_height()
        elif self.key < node.key:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
            self.update_height()
        else:
            self.value = node.value

        # print("My height is " + str(self.height))

    def swap(self, other):
        super().swap(other)
        self.height, other.height = other.height, self.height
    
    def remove(self, key):
        # there is nothing that can really be done with the height of this key
        if self.key == key:
            if self.right is None: 
                return self.left
            if self.left is None:
                return self.right
            replacement = self.right.minimum()
            self.swap(replacement)
            self.right = self.right.remove(key)

        # remove from left subtree
        elif self.key > key and self.left is not None:
            self.left = self.left.remove(key)
            self.update_height()
        # remove from the right subtree
        elif self.key < key and self.right is not None:
            self.right = self.right.remove(key)
            self.update_height()
        # key is not in the tree
        else:
            raise KeyError('delete on a non-existent key!')

        # print("My height is " + str(self.height))
        return self

    '''
    This is where things start to get messy
    Buckle up because this is gonna be a bumpy ride!
    '''
    # def rotate1
    # def rotate2

    def __repr__(self):
        return f"[<{self.key},{self.value},{self.height}> : {repr(self.left)}, {repr(self.right)}]"


class AVL(BST):
    node = AVLNode
    def __init__(self):
        super().__init__()
