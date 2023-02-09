count = x = int(input(''))
y = int(x*(x+1)/2)


def fact(x, y, count):
    if count == 0:
        return print(x, y)
    else:
        x += (count-1)
    count -= 1
    fact(x, y, count)


fact(x, y, count)
