import unittest

from tests import test_tree
from DS import BST

class TestBST(unittest.TestCase, test_tree.TestTree):
    def maketree(self):
        return BST()

if __name__ == '__main__':
    unittest.main()