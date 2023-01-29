parse_list = list(
    filter(str, input('Введите слова через пробел ').split()))
print(parse_list)
i = 0
while i < len(parse_list):
    print(f'{i+1}.{parse_list[i]:.10}')
    i += 1
