"""
Сортировка вставками.
"""
import typing as tpg


def insertion_sort(seq: tpg.Iterable, reverse: bool = False) -> tpg.List:
    """
    Сортировка вставками.

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

    for i in range(len(seq_copy) - 1):
        swap = (not reverse and seq_copy[i] > seq_copy[i + 1]) or (reverse and seq_copy[i] < seq_copy[i + 1])
        if swap:
            seq_copy[i], seq_copy[i + 1] = seq_copy[i + 1], seq_copy[i]

        if i > 0 and swap:
            # для первого элемента, даже если была перестановка,
            # предыдущего элемента нет, поэтому проверяем > 0
            for j in range(i, 0, -1):
                # идем к началу массива
                swap = (not reverse and seq_copy[j] < seq_copy[j - 1]) or (reverse and seq_copy[j] > seq_copy[j - 1])
                if swap:
                    seq_copy[j], seq_copy[j - 1] = seq_copy[j - 1], seq_copy[j]
                else:
                    # если перестановка не нужна, то оставшаяся часть в начале последовательности
                    # уже отсортирована
                    break
    return seq_copy
