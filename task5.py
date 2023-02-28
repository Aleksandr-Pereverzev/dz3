# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n)
# самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число 
#  N –  количество элементов в массиве. Последняя строка содержит число X



n = int(input('введите число'))

import random
rand_list=[]
for i in range(n):
    rand_list.append(random.randint(1,9))
print(rand_list)

m = int(input('введите второе число'))

res = rand_list[0]
for i in rand_list:
    if abs(i - m) < abs(res - m):
        res = i

print(res)

