# Требуется вычислить, сколько раз встречается некоторое число X в массиве из случайных чисел. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1




n = int(input('введите число'))

import random
rand_list=[]
for i in range(n):
    rand_list.append(random.randint(1,9))
print(rand_list)

n = int(input('какое число ищем: '))

print (rand_list.count(n))