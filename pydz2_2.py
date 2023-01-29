print('давай, жги число')
user_number = int(input())
max_number = 0
temp_number = 0
while user_number > 1:
    temp_number = user_number % 10
    user_number //= 10
    if temp_number > max_number:
        max_number = temp_number
print(max_number)
