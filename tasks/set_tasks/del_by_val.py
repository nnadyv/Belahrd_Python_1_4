"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая удалит элемент по его значению
"""
from typing import Any


def del_by_value(collection: set, value: Any) -> set:
    collection.remove(value)# TODO вставить код сюда
    return collection


if __name__ == '__main__':
    assert 5 not in del_by_value({1, 3, 5, 2}, 5)
    print('Решено!')
