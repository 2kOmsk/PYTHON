i = int(input('i = '))
j = int(input('j = '))


def get_ascii(i, j, count=0):
    if i > j:
        return
    else:
        print(i, "-", chr(i), end='\t')
        count += 1
        if count % 10 == 0:
            print()
        get_ascii(i+1, j, count)


get_ascii(i, j)
