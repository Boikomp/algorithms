x1 = float(input('Введите координату X первой точки: '))
y1 = float(input('Введите координату Y первой точки: '))
x2 = float(input('Введите координату X второй точки: '))
y2 = float(input('Введите координату Y второй точки: '))

if x1 == x2:
    print(f'Уравнение прямой: x = {x1}')
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    input(f'Уравнение прямой: y = {k}*x + {b}')