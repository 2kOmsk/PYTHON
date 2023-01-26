"""
Задание 1.
"""
print('hi, insert you Name')
a = input()
print('hi, insert you pass')
b = input()
print('hi, insert you age')
c = input()
print(f'Ваши данные для входа в аккаунт: имя - {a}, пароль - {b}, возраст - {c}')

"""
Задание 2.
"""
print('hi, insert time, format sec')
a =  input() 
b = int(a) / 60 / 60
c = int(a) / 60
print(f'Время в формате ч:м:с  {round(b,2)} :  {round(c,2)}, :  {a}')
"""
Задание 3.
"""
print('hi, insert number, n')
n =  input() 
m = (int(n) + int(n+n) + int(n+n+n))
print(f'Summ of n + nn + nnn: = {m}')

"""
Задание 4.
"""
print('Введите выручку фирмы: ')
value =  int(input()) 
print ('Введите расходы фирмы: ')
expire =  int(input()) 
prof = value - expire
if  prof > 0:
    print('Введите численность сотрудников фирмы: ')
    worker =  int(input())
    pworker = int(prof / worker)
    print(f'Ваша прибыль: = {prof}, Доход на сотрудника : {round(pworker,2)}')
else:
    print(f'У вас нет  прибыли, пора  что то менять!')