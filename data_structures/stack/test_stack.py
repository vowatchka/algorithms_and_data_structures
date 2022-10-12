import unittest

from data_structures.stack import stack


class TestStack(unittest.TestCase):
    def test_init(self):
        """
        Проверка инициализации стэка.
        """
        stack_ = stack.Stack()
        self.assertIsInstance(stack_, stack.Stack)
        self.assertEqual(len(stack_), 0)

    def test_push(self):
        stack_ = stack.Stack()
        stack_.push(1)
        stack_.push("2")

        self.assertEqual(len(stack_), 2)
        self.assertEqual(list(stack_), ["2", 1])

    def test_pop(self):
        stack_ = stack.Stack()
        stack_.push(1)
        stack_.push("2")
        stack_.push(3)

        item = stack_.pop()
        self.assertEqual(item, 3)
        self.assertEqual(len(stack_), 2)
        self.assertEqual(list(stack_), ["2", 1])

        item = stack_.pop()
        self.assertEqual(item, "2")
        self.assertEqual(len(stack_), 1)
        self.assertEqual(list(stack_), [1])

    def test_pop_from_empty(self):
        stack_ = stack.Stack()
        stack_.push(1)

        stack_.pop()

        with self.assertRaises(IndexError):
            stack_.pop()

    def test_top(self):
        stack_ = stack.Stack()
        stack_.push(1)
        stack_.push("2")
        stack_.push(3)

        item = stack_.top()
        self.assertEqual(item, 3)
        self.assertEqual(len(stack_), 3)

    def test_top_from_empty(self):
        stack_ = stack.Stack()

        with self.assertRaises(stack.EmptyStackError):
            stack_.top()

    def test_clear(self):
        stack_ = stack.Stack()
        stack_.push(1)
        stack_.push("2")

        stack_.clear()
        self.assertEqual(len(stack_), 0)
        self.assertEqual(list(stack_), [])
