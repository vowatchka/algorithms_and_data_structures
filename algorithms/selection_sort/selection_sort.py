"""
Сортировка выбором.
"""
import typing as tpg


def selection_sort(seq: tpg.Iterable, reverse=False) -> tpg.List:
    """
    Сортировка выбором.

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

    for i, item in enumerate(seq_copy):
        min_max_idx, min_max_value = None, item
        for j in range(i + 1, len(seq_copy)):
            # ищем минимальное или максимальное значение в оставшейся части последовательности
            # (в зависимости от направления сортировки)
            if ((not reverse and seq_copy[j] < min_max_value)
                    or (reverse and seq_copy[j] > min_max_value)):
                min_max_idx, min_max_value = j, seq_copy[j]

        if min_max_idx:
            # если нашли новое минимальное значение
            seq_copy[i], seq_copy[min_max_idx] = min_max_value, item

    return seq_copy
