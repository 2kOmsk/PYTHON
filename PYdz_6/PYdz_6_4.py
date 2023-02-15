list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

result = [i for i in list_numbers if list_numbers.count(i) == 1]

print(result)
