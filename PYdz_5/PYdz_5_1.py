a = int(input('first num a: '))
b = int(input('second num b: '))
oper = input('operation: ')
def calk(a, b, oper):
    if oper == '/' and b == 0:
        print('debil allert')
    else:
        if oper == "/": a /= b
        if oper == "*": a *= b
        if oper == "-": a -= b
        if oper == "+": a += b
        return a
calc_res = print(calk(a, b, oper))
