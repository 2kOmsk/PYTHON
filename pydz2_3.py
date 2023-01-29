print('парисим классы')
spisok = [5, "string", 0.15, True, None]
i = 0
while 0 < len(spisok):
    v = spisok.pop()
    print(type(v))
    i += 1
