import random
import unittest

from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def setUp(self) -> None:
        self.seq = list(range(10))
        random.shuffle(self.seq)

    def test_empty_seq(self):
        """
        Проверка на пустой последовательности.
        """
        sorted_seq = selection_sort([])
        self.assertEqual(len(sorted_seq), 0)

    def test_sort(self):
        """
        Проверка сортировки.
        """
        sorted_seq = selection_sort(self.seq)
        self.assertEqual(sorted_seq, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_bubble_sort_immutable(self):
        """
        Проверка, что функция быстрой сортировки не изменяет исходную
        последовательность.
        """
        sorted_seq = selection_sort(self.seq)
        self.assertNotEqual(self.seq, sorted_seq)

    def test_reverse(self):
        """
        Проверка сортировки по убыванию.
        """
        sorted_seq = selection_sort(self.seq, reverse=True)
        self.assertEqual(sorted_seq, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_sort_tuple(self):
        """
        Проверка сортировки последовательности другого типа (tuple).
        """
        sorted_seq = selection_sort(tuple(self.seq))
        self.assertIsInstance(sorted_seq, list)
        self.assertEqual(sorted_seq, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_sort_generator(self):
        """
        Проверка сортировки последовательности другого типа (generator).
        """
        sorted_seq = selection_sort(x for x in self.seq)
        self.assertIsInstance(sorted_seq, list)
        self.assertEqual(sorted_seq, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_sorted(self):
        """
        Проверка на отсортированной последовательности.
        """
        sorted_seq = selection_sort(sorted(self.seq))
        self.assertEqual(sorted_seq, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_sorted_reverse(self):
        """
        Проверка на последовательности отсортированной в обратном порядке.
        """
        sorted_seq = selection_sort(sorted(self.seq, reverse=True), reverse=True)
        self.assertEqual(sorted_seq, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
