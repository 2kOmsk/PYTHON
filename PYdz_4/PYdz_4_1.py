user_num1 = int(input('Введите первое число: '))
user_num2 = int(input('Введите второе число: '))


def my_div(user_num1, user_num2):
    return user_num1 / user_num2


if user_num2 != 0:
    print(my_div(user_num1, user_num2))
else:
    print('Дурак detected')
