import itertools
import unittest

from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_empty_seq(self):
        """
        Проверка пустой последовательности.
        """
        idx = binary_search([], 1)
        self.assertIsNone(idx)

    def test_not_found(self):
        """
        Проверка, когда элемент не найден.
        """
        idx = binary_search([1, 2, 3], 4)
        self.assertIsNone(idx)

    def test_found(self):
        """
        Проверка, когда элемент найден.
        """
        idx = binary_search(range(0, 20, 2), 8)
        self.assertEqual(idx, 4)

    def test_reverse(self):
        """
        Проверка поиска, когда последовательность отсортирована по убыванию.
        """
        seq = sorted(range(0, 20, 2), reverse=True)

        idx = binary_search(seq, 8, reverse=True)
        self.assertEqual(idx, 5)

    def test_string_items(self):
        """
        Проверка с последовательностью из строк.
        """
        seq = sorted(("Nigel Rees", "Evelyn Waugh", "Herman Melville", "J. R. R. Tolkien"))

        idx = binary_search(seq, "Herman Melville")
        self.assertEqual(idx, 1)

    def test_list_items(self):
        """
        Проверка с последовательностью из списков.
        """
        seq = ("".join(x) for x in itertools.product("ABC", "xyz"))

        idx = binary_search(seq, "Bz")
        self.assertEqual(idx, 5)
