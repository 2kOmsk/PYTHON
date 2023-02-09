num1 = int(input('число 1: '))
num2 = int(input('число 2: '))
num3 = int(input('число 3: '))


def my_func(num1, num2, num3):
    num_sum = 0
    if num1 < num2:
        if num1 < num3:
            num_sum = num2 + num3
        else:
            num_sum = num2 + num1
    elif num2 < num3:
        num_sum = num1 + num3
    else:
        num_sum = num1 + num2
    return num_sum


v = my_func(num1, num2, num3)
print(v)
