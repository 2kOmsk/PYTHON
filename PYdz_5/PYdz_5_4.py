n = int(input('Введите количество элементов n : '))


def my_func(n):
    i = n
    if i == 0:
        return n
    else:
        return pow(-0.5, n-1) + my_func(n-1)


print(f'Количество элементов - {n}, их сумма - {my_func(n)}')
