user_num = int(input('Введите число, которое требуется перевернуть: '))


def parse_num(num, salto_num=0):
    if num == 0:
        return str(num)
    if num % 10 > 0 or num % 10 == 0:
        return str(num % 10) + str(parse_num(num // 10))


print(f'Перевернутое число: {parse_num(user_num)}')
