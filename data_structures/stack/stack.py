"""
Стэк.

>>> stack = Stack()
>>> stack.push("a")
>>> stack.push("b")
>>> len(stack)
2
>>> list(stack)
['b', 'a']
>>> stack.top()
'b'
>>> item = stack.pop()
>>> item
'b'
>>> len(stack)
1
>>> stack.top()
'a'
>>> stack.clear()
>>> len(stack)
0
>>> stack.pop()
Traceback (most recent call last):
...
IndexError: pop from empty stack
>>> stack.top()
Traceback (most recent call last):
...
TypeError: stack is empty
"""
import typing as tpg


class Item:
    """
    Элемент стэка.
    """
    def __init__(self, value: tpg.Any, next_item: tpg.Optional["Item"] = None):
        self.value = value
        self.next_item = next_item


class Stack:
    """
    Стэк.

    Реализация на основе односвязного списка.
    """

    def __init__(self):
        self._head: tpg.Optional[Item] = None
        self._len: int = 0

    def __len__(self):
        return self._len

    def __iter__(self):
        self.__item = self._head
        return self

    def __next__(self):
        if not self.__item:
            raise StopIteration

        value = self.__item.value
        self.__item = self.__item.next_item

        return value

    def push(self, value: tpg.Any):
        """
        Добавить элемент на вершину стэка.

        :param value: значение элемента
        """
        item = Item(value)

        if self._head:
            # новый элемент получает ссылку на текущую голову стэка
            item.next_item = self._head

        # новый элемент становится новой головой стэка
        self._head = item

        self._len += 1

    def pop(self) -> tpg.Any:
        """
        Снять элемент с вершины стэка и вернуть его.
        """
        if not self._head:
            raise IndexError("pop from empty stack")

        item = self._head
        # Следующий за головой элемент становится новой головой
        self._head = item.next_item
        # у удаляемого элемента очищаем ссылку на элемент
        item.next_item = None

        self._len -= 1

        return item.value

    def top(self) -> tpg.Any:
        """
        Вернуть верхний элемент стэка.
        """
        if not self._head:
            raise TypeError("stack is empty")

        return self._head.value

    def clear(self):
        """
        Очистить стэк.
        """
        # удаляем голову
        # остальные элементы стэка должен удалить сборщик мусора
        # TODO: сделать очистку стэка не полагаясь на сборщик мусора
        self._head = None
        self._len = 0
