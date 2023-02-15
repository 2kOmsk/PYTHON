from functools import reduce

list_numbers = [i for i in range(10, 101) if i % 2 == 0]

result = reduce(lambda x, y: x + y, list_numbers)

print(result)