user_element = int(input('давай сыграем в игру :'))
element_rating = [7, 5, 3, 3, 2]
element_rating.append(user_element)
element_rating.sort(reverse=True)
print(f'вы ввели{user_element}, рейтинг после ввода: {element_rating}')