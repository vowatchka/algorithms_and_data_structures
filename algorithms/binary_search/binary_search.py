"""
Бинарный поиск.
"""
import typing as tpg


def binary_search(seq: tpg.Iterable, searched: tpg.Any, reverse: bool = False) -> tpg.Optional[int]:
    """
    Бинарный поиск.

    Элементы в последовательности должны быть предварительно отсортированы и
    поддерживать операции сравнения (==, !=, >, <, >=, <=).

    :param seq: отсортированная последовательность, в которой будет производиться бинарный поиск
    :param searched: искомое значение
    :param reverse: `False` - последовательность отсортирована по возрастанию;
        `True` - последовательность отсортирована по убыванию
    :return: индекс искомого значения или `None`, если значение не было найдено
    """
    seq_copy = tuple(seq)

    # границы поиска
    low = 0
    high = len(seq_copy) - 1

    while low <= high:
        # индекс срединного элемента
        mid = (low + high) // 2
        # срединный элемент
        mid_item = seq_copy[mid]

        if mid_item == searched:
            return mid
        elif mid_item > searched:
            if reverse:
                # продолжаем поиск правее срединного элемента
                low = mid + 1
            else:
                # продолжаем поиск левее срединного элемента
                high = mid - 1
        else:
            if reverse:
                # продолжаем поиск левее срединного элемента
                high = mid - 1
            else:
                # продолжаем поиск правее срединного элемента
                low = mid + 1
    else:
        return None
