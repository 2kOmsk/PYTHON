from timeit import timeit

def my_func(*args):
    temp_mass = []
    temp_mass.append(int(input('число 1: ')))
    temp_mass.append(int(input('число 2: ')))
    temp_mass.append(int(input('число 3: ')))
    temp_mass.sort(reverse=True)
    num_sum = temp_mass[0] + temp_mass[1]
print(timeit("my_func()", globals=globals(), number=1000))