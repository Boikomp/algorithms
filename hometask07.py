n = int(input('Введите натуральное число n: '))

i = 0
left = 0

while i < n:
    i += 1
    left += i

right = n * (n + 1) / 2

if right == left:
    print('Эврика. Гипотеза верна.')
else:
    print('Гипотеза не верна.')
