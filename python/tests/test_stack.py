import unittest
from random import randint

from DS import stack

class TestStack(unittest.TestCase):
    def test_stack_top(self):
        s = stack.Stack()
        num = randint(0, 100000000)
        s.push(num)
        self.assertEqual(s.top(), num)

    def test_stack_empty(self):
        s = stack.Stack()
        num = randint(0, 100000000)
        s.push(num)
        self.assertFalse(s.empty())
        s.pop()
        self.assertTrue(s.empty())

    def test_push_and_pop(self):
        s = stack.Stack()
        for i in range(1000):
            s.push(randint(0, 2**32))
        self.assertFalse(s.empty())
        for i in range(1000):
            s.pop()
        self.assertTrue(s.empty())

    def test_empty_pop(self):
        s = stack.Stack()
        self.assertRaises(IndexError, s.pop)

    def test_empty_top(self):
        s = stack.Stack()
        self.assertRaises(IndexError, s.top)

if __name__ == '__main__':
    unittest.main()

