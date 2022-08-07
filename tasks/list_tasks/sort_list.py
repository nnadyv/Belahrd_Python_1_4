"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернет 2 списка, один отсортированные по возрастанию,
а второй по убыванию
"""
from copy import deepcopy


def sort_list(collection: list) -> tuple:
    asc_sort = deepcopy(collection)
    desc_sort = deepcopy(collection)
    desc_sort.sort(reverse=True)
    asc_sort.sort(reverse=False)  # TODO вставить код сюда
    return asc_sort, desc_sort


if __name__ == '__main__':
    assert ([1, 2, 3], [3, 2, 1]) == sort_list([3, 1, 2])
    print('Решено!')
