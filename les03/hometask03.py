# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_i = 0
min_i = 0

for i in range(len(array)):
    if array[i] < array[min_i]:
        min_i = i
    elif array[i] > array[max_i]:
        max_i = i

# print(f'{max_i=}, {min_i=}')

spam = array[max_i]
array[max_i] = array[min_i]
array[min_i] = spam

print(array)
