# https://drive.google.com/open?id=1JHA_XScaLbhu1kWMFbaM3PtAw9rUeY7f

while True:
    simbol = input('Введите знак операции(+,-,*,/). Для выхода введите 0: ')
    if simbol == '0':
        break
    elif simbol in ('+', '-', '*', '/'):
        x = float(input('Введите первое число: '))
        y = float(input('Введите второе число: '))
        if simbol == '+':
            print(f'Ответ: {x + y}')
        elif simbol == '-':
            print(f'Ответ: {x - y}')
        elif simbol == '*':
            print(f'Ответ: {x * y}')
        else:
            if y == 0:
                print('Деление на ноль запрещено!')
            else:
                print(f'Ответ: {x / y}')
    else:
        print('Неизвестный символ операции!')
