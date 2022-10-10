import unittest

from stack import Stack


class TestStack(unittest.TestCase):
    def test_init(self):
        """
        Проверка инициализации стэка.
        """
        stack = Stack()
        self.assertIsInstance(stack, Stack)
        self.assertEqual(len(stack), 0)

    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push("2")

        self.assertEqual(len(stack), 2)
        self.assertEqual(list(stack), ["2", 1])

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push("2")
        stack.push(3)

        item = stack.pop()
        self.assertEqual(item, 3)
        self.assertEqual(len(stack), 2)
        self.assertEqual(list(stack), ["2", 1])

        item = stack.pop()
        self.assertEqual(item, "2")
        self.assertEqual(len(stack), 1)
        self.assertEqual(list(stack), [1])

    def test_pop_from_empty(self):
        stack = Stack()
        stack.push(1)

        stack.pop()

        with self.assertRaises(IndexError):
            stack.pop()

    def test_top(self):
        stack = Stack()
        stack.push(1)
        stack.push("2")
        stack.push(3)

        item = stack.top()
        self.assertEqual(item, 3)
        self.assertEqual(len(stack), 3)

    def test_top_from_empty(self):
        stack = Stack()

        with self.assertRaises(TypeError):
            stack.top()

    def test_clear(self):
        stack = Stack()
        stack.push(1)
        stack.push("2")

        stack.clear()
        self.assertEqual(len(stack), 0)
        self.assertEqual(list(stack), [])
