# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно
# ввести с клавиатуры. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Пример:
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


# a = int(input("Введите начальное число:"))
# n = int(input("Введите количество элементов: "))
# d = int(input("Введите число на которое увеличивать прогрессию: "))
# pro = []
# for i in range(n):
#     pro.append(a + i * d)
# print(*pro)

# ------------------------------------------------------------------------

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Пример:
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

max_array = int(input("Введите максимальное значение диапазона: "))
min_array = int(input("Введите минимальное значение диапазона: "))
result = []

if max_array >= min_array:
    for i in range(len(array)):
        if max_array >= array[i] and min_array <= array[i]:
            result.append(i)
    print(result)
