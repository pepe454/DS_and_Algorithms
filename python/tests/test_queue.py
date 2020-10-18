import unittest
from random import randint

from DS import Queue

class TestQueue(unittest.TestCase):
    def test_empty(self):
        q = Queue()
        self.assertTrue(q.empty())
        q.enqueue(randint(0, 2**32))
        self.assertFalse(q.empty())

    def test_enqueue_and_dequeue(self):
        q = Queue()
        for i in range(1000):
            q.enqueue(randint(0, 2**32))
        self.assertFalse(q.empty())
        self.assertEqual(len(q), 1000)
        for i in range(1000):
            q.dequeue()
        self.assertEqual(len(q), 0)
        self.assertTrue(q.empty())

        self.assertRaises(IndexError, q.peek_front)
        self.assertRaises(IndexError, q.peek_back)
        self.assertRaises(IndexError, q.dequeue_front)
        self.assertRaises(IndexError, q.dequeue)

    def test_enqueue_back_and_dequeue_front(self):
        q = Queue()
        for i in range(1000):
            q.enqueue_back(randint(0, 2**32))
        self.assertFalse(q.empty())
        self.assertEqual(len(q), 1000)
        for i in range(1000):
            q.dequeue_front()
        self.assertTrue(q.empty())
        self.assertEqual(len(q), 0)

        self.assertRaises(IndexError, q.peek_front)
        self.assertRaises(IndexError, q.peek_back)
        self.assertRaises(IndexError, q.dequeue_front)
        self.assertRaises(IndexError, q.dequeue)

    def test_input_output_restrictions(self):
        q = Queue(True, True)
        self.assertRaises(Exception, q.enqueue_back)
        self.assertRaises(Exception, q.dequeue_front)
        num = randint(0, 2**32)
        q.enqueue(num)
        self.assertFalse(q.empty())
        test_num = q.dequeue()
        self.assertTrue(q.empty())
        self.assertEqual(num, test_num)

    def test_peek(self):
        q = Queue()
        num = randint(0, 100000000)
        q.enqueue(num)
        self.assertEqual(q.peek_front(), num)
        self.assertEqual(q.peek_back(), num)
        self.assertEqual(len(q), 1)
        q.enqueue(num + 1)
        q.enqueue_back(num - 1)
        self.assertEqual(q.peek_front(), num + 1)
        self.assertEqual(q.peek_back(), num - 1)
        self.assertEqual(len(q), 3)

if __name__ == '__main__':
    unittest.main()

