parse_number = list(
    filter(int, input('Введите числа через пробел ').split()))
temp_parse = parse_number.copy()
i = 0
while i+1 < len(parse_number):
    if i+1 != None:
        temp_parse[i] = parse_number[i+1]
        temp_parse[i+1] = parse_number[i]
        i += 2
        print(temp_parse)
    else:
        print(temp_parse)
