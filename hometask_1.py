# https://drive.google.com/file/d/1DJ9vHDwiN7W03x-UUspn4ZVmQiwCkI7F/view?usp=sharing
x = int(input('Введите трехзначное число: '))

a = x // 100
b = x // 10 % 10
c = x % 10

sum = a + b + c
mult = a * b * c

print(f'Сумма цифр {sum}, произведение цифр {mult}')
