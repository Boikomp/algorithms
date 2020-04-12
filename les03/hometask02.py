# Во втором массиве сохранить индексы четных элементов первого массива.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

res = []

for i, item in enumerate(array):
    if item % 2 == 0:
        res.append(i)

print(res)
