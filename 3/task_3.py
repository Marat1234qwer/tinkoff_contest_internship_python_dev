"""
Водим данные.
Разбиваем введеные строки на папки по символу '/'.
Сортируем список.
Выводим папки на печать.
"""


def action_partition(lst, lst_partition):  # заполняем список названиями папок, убираем знак '/'
    if lst.count('/'):
        for _ in range(lst.count('/')):
            folder = lst.partition('/')[0]
            lst_partition.append(folder)
            action_partition(lst.partition('/')[2], lst_partition)
            break
    else:
        lst_partition.append(lst)
    return lst_partition


def main():
    n = int(input())
    lst_folder = []
    for i in range(n):
        lst_insert = input()
        lst_folder.append(lst_insert)

    lst_partition_total = []  # список названий папок
    for i in range(n):
        lst_partition = []
        lst_partition = action_partition(lst_folder[i], lst_partition)
        lst_partition_total.append(lst_partition)
    lst_partition_total.sort()

    root = lst_partition_total[0]  # первый элемент списка
    for i in range(n):
        if lst_partition_total[i] == root:
            print(root[0])
        else:
            index = lst_partition_total[i].index(lst_partition_total[i][len(lst_partition_total[i])-1])  # количество двойных пробелов
            print('  '*index, lst_partition_total[i][len(lst_partition_total[i])-1])


if __name__ == '__main__':
    main()
