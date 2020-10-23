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
