# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

ROW = 5
COLUMN = 4

array = [[0] * COLUMN for _ in range(ROW)]

for i in range(ROW):
    sum_row = 0
    for j in range(COLUMN):
        if j != COLUMN - 1:
            array[i][j] = int(input(f'Введите элемент {j + 1} строки {i + 1}: '))
            sum_row += array[i][j]
        else:
            array[i][j] = sum_row

print(*array, sep='\n')
