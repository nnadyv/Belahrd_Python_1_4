"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Электронная очередь.

Имеется список посетителей. Чтобы подозвать человека к окошку - нужно удалить
последнего посетителя из списка и вернуть его номерок
"""
client_list = [123, 321, 213]


def del_last(collection: list) -> int:
    collection = client_list.pop()
    list1 = collection.insert(2, client_list)  # TODO вставить код сюда
    result = list1
    return result


if __name__ == '__main__':
    print("Ту ду ду")
    print(f"Клиент номер {del_last(client_list)}, подойдите к окошку номер 3")
