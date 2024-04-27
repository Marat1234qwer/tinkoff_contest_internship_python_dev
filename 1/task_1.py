"""
Вводим данные. Создаем список списков семи оценок подряд.
Затем делаем проверку на '2' и '3'.
Считаем количество пятерок в списках.
Выводим на печать наибольшее количество пятерок.
"""
n = int(input())
lst = list(map(int, input().split()))

l_seven = 7
lst_seventh = []  # список списков оценок
for i in range(len(lst)-6):
    lst_insert = []  # список семи оценок подряд
    for j in range(l_seven):
        lst_insert.append(lst[j+i])
    lst_seventh.append(lst_insert)

for i in range(len(lst_seventh)):  # проверка если 2 и 3, то список меняем на None
    if lst_seventh[i].count(3) or lst_seventh[i].count(2):
        lst_seventh[i] = None

empty = 0
lst_five = []
for i in range(len(lst_seventh)):
    if lst_seventh[i] is None:
        empty += 1
    else:
        five_count = 0
        for j in range(l_seven):  # считаем пятерки
            if lst_seventh[i][j] == 5:
                five_count += 1
        lst_five.append(five_count)

if len(lst_seventh) == empty:
    print(-1)
else:
    print(max(lst_five))  # выводим на печать максимум пятерок
