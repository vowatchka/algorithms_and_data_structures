"""
Пузырьковая сортировка.
"""
import typing as tpg


def bubble_sort(seq: tpg.Iterable, reverse: bool = False) -> tpg.List:
    """
    Пузырьковая сортировка.

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

    for i, _ in enumerate(seq_copy):
        for j in range(len(seq_copy) - i - 1):
            if ((not reverse and seq_copy[j] > seq_copy[j + 1])
                    or (reverse and seq_copy[j] < seq_copy[j + 1])):
                seq_copy[j], seq_copy[j + 1] = seq_copy[j + 1], seq_copy[j]
    return seq_copy
