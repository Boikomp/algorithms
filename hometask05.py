for i in range(32, 128):
    x = chr(i)
    if (i - 31) % 10 == 0:
        print(f'{i}-{x}')
    else:
        print(f'{i}-{x}', end=' ')
