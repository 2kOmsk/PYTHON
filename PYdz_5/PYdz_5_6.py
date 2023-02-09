import random
prog_rand = random.randint(0, 100)


def ugadai(prog_rand, user_num=0, count=1):
    user_num = int(input(f'попытка № {count}: '))
    if count < 10:
        if user_num < prog_rand:
            print('мое число больше')
        elif user_num == prog_rand:
            return print('Поздравлямба, ты первый после бога')
        else:
            print('мое число меньше')
        count += 1
        ugadai(prog_rand, user_num, count)
    else:
        return print('Тебя сделали мешок  костей, я загадал: ', prog_rand)


ugadai(prog_rand)
