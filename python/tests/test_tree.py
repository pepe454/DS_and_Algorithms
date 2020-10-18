from random import randint

# parent testing class for all trees
class TestTree:
    def maketree(self):
        raise NotImplementedError

    def test_insert_and_search(self):
        tree = self.maketree()
        nums = {randint(0, 2**16) for i in range(1000)}
        # the values do not matter
        for key in nums:
            tree.insert(key, 'nodevalue')
        for key in nums:
            self.assertEqual(tree.search(key), 'nodevalue')

    def test_insert_and_remove(self):
        tree = self.maketree()
        nums = {randint(0, 2**16) for i in range(1000)}
        # the values do not matter
        for key in nums:
            tree.insert(key, 'nodevalue')
        for key in nums:
            tree.remove(key)
            self.assertRaises(KeyError, tree.search, key)

        self.assertIsNone(tree._root)

'''
bst = BST()
bst.insert(10, 'n1')
bst.insert(5, 'n2')
bst.insert(4, 'n3')
bst.insert(6, 'n4')
bst.insert(14, 'n5')
bst.insert(11, 'n6')
bst.insert(12, 'n7')
bst.insert(16, 'n8')
bst.insert(15, 'n9')

STRUCTURE of bst
        10 
      /   \\
     5     14
   /  \    /  \ 
  4   6   11   16
           \   / 
           12  15
'''