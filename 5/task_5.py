"""
Вводим данные.
Меняем 'W' на -1, 'C' на 1, '.' на 0.
Проходимся по списку и увеличиваем значение на 1 если
следующяя клетка на которую наступаем
по диагонали и на ней '1'.
Выводим на печать максимум последней строки.
"""

n = int(input())

lst_way = []
for i in range(n):
    lst_insert = input()
    lst_way.append(lst_insert)

#  сосдаем список, переводим буквы в цифры
lst_numbers = []
for i in range(n):
    lst_insert = [0] * 3
    for j in range(3):
        if lst_way[i][j] == 'W':
            lst_insert[j] = -1
        elif lst_way[i][j] == 'C':
            lst_insert[j] = 1
    lst_numbers.append(lst_insert)

#  список посещенных клеток
lst_visited = [[-1] * 3] * 5
lst_visited[0] = lst_numbers[0]

for i in range(1, n):
    for j in range(3):
        for v in range(3):
            if j + v < 3 and lst_visited[i-1][j+v] != -1 and lst_numbers[i][j] != -1:
                lst_visited[i][j] = max(lst_visited[i][j], lst_visited[i-1][j+v]+lst_numbers[i][j])

print(max(lst_visited[-1]))
