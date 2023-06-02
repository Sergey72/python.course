# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


# n = int(input('Количество элементов первого множества? '))
# many1 = set()
# for i in range(n):
#     many1.add(input())
# print('Множество:', many1)
# m = int(input('Количество элементов второго множества? '))
# many2 = set()
# for i in range(m):
#     many2.add(input())
# print('Множество:', many2)

# strit = []
# for i in many1:
#     for j in many2:
#         if i == j:
#             strit.append(i)
# print(*strit)

#--------------------------------------------------------------------


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

#  Пример:
# 4 -> 1 2 3 4
# 9

bed = [1, 2, 3, 4]
sumif = 0
max_sum = 0
temp = 0
for i in range(len(bed)):
    sumif = sum(bed[:3])
    temp = (bed.pop())
    bed.insert(0, temp)
    if sumif > max_sum:
        max_sum = sumif
    i += 1
print(max_sum)
