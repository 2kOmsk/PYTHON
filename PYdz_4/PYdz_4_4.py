x = int(input('input X: '))
y = int(input('input Y: '))


def my_func(x, y):
    i = y*(-1)
    x = 1/(x*i)
    return x


degree = my_func(x, y)
print(degree)
