user_num = int(input('парсим цифры: '))


def parse_num(num, m_count=0, p_count=0):
    if num < 1:
        return m_count, p_count
    if num % 10 % 2 == 1:
        p_count += 1
    else:
        m_count += 1
    return parse_num(num // 10, m_count, p_count)


print(parse_num(user_num))
