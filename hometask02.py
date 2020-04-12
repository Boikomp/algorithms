x = str(input('Введите натуральное число: '))

even = 0
odd = 0

for i in x:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'В числе {x} {even} четных и {odd} нечетных цифр.')
