"""
Быстрая сортировка.
"""
import typing as tpg


def quick_sort(seq: tpg.Iterable, reverse=False) -> tpg.List:
    """
    Быстрая сортировка.

    :param seq: последовательность, которую нужно отсортировать
    :param reverse: `False` - последовательность сортируется по возрастанию;
        `True` - последовательность сортируется по убыванию
    :return: отсортированная последовательность
    """
    seq_copy = list(seq)
    if len(seq_copy) < 2:
        # если в последовательности один элемент или она пуста,
        # то можно считать последовательность уже отсортированной
        return seq_copy

    # опорный элемент
    # TODO: стоит выбирать более лучший опорный элемент, нежели самый первый
    pivot = seq_copy[0]

    # все элементы меньше опорного
    less = quick_sort((x for x in seq_copy if x < pivot), reverse=reverse)
    # все элементы больше опорного
    greater = quick_sort((x for x in seq_copy if x > pivot), reverse=reverse)

    if reverse:
        return greater + [pivot] + less
    else:
        return less + [pivot] + greater
