# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

res = MIN_ITEM - 1
res_i = -1

for i in range(len(array)):
    if array[i] < 0 and array[i] > res:
        res = array[i]
        res_i = i

if res_i == -1:
    print('Отрицательных элементов в массиве нет.')
else:
    print(f'Максимальный отрицательный элемент массива: {res}, его позиция: {res_i}')
