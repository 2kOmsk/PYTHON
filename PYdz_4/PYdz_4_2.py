def user_add_info(**args):
    user_info = {
        1: input('имя: '),
        2: input('фамилия: '),
        3: input('дата рождения: '),
        4: input('город проживания: '),
        5: input('mail: '),
        6: input('телефон: ')
    }
    return user_info


v = user_add_info()
print(f'{v[2]} {v[1]} {v[3]} года рождения, проживает в г.{v[4]}, email: {v[5]}, телефон: {v[6]}')
