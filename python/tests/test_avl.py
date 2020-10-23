import unittest

from tests import test_tree
from DS import AVL
from DS import Stack
from Algorithms import inorder

class TestBST(unittest.TestCase, test_tree.TestTree):
    def maketree(self):
        return AVL()

    def test_tree_heights(self):
        avl = self.maketree()
        avl.insert(10, 'n1')
        avl.insert(5, 'n2')
        avl.insert(4, 'n3')
        avl.insert(6, 'n4')
        avl.insert(14, 'n5')
        avl.insert(11, 'n6')
        avl.insert(12, 'n7')
        avl.insert(16, 'n8')
        avl.insert(15, 'n9')

        '''
        STRUCTURE of avl
                10 
            /   \\
            5     14
        /  \    /  \ 
        4   6   11   16
                \   / 
                12  15
        '''
        inorder_list = inorder(avl._root)
        heights = [1, 2, 1, 4, 2, 1, 3, 1, 2]
        for height, node in zip(heights, inorder_list):
            self.assertEqual(height, node.height)

if __name__ == '__main__':
    unittest.main()