list_numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [list_numbers[i] for i in range(
    1, len(list_numbers)) if list_numbers[i] > list_numbers[i-1]]

print(result)  # [12, 44, 4, 10, 78, 123]
