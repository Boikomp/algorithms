def recursion(n):
    global a, i, res
    if i < n:
        a = a / -2
        res += a
        i += 1
        return recursion(n)
    else:
        return res


n = int(input('Введите количество элементов ряда: '))

i = 0
a = 1
res = 1

print(recursion(n - 1))
