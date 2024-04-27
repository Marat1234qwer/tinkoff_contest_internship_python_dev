"""
Вводим данные:
n - количество строк,
m - количество столбцов,
считываем матрицу.
Поворачиваем матрицу, выводим на печать.
"""
n, m = map(int, input().split())

lst_mtrx = []
for i in range(n):
    lst_string = list(map(int, input().split()))
    lst_mtrx.append(lst_string)
lst_route = [[0] * n for i in range(m)]

for i in range(n):  # алгоритм поворота матрицы
    for j in range(m):
        lst_route[j][n-1-i] = lst_mtrx[i][j]
        
for item in lst_route:
    print(*item)
