print('Введите текущий результат в км: ')
dis_result = int(input())
print('Введите цель в км: ')
dis_target = int(input())
day_count = 1
daily_up = 1.1
print(f'результат:\n{day_count}-й день : {dis_result:.2f} км')
while dis_result < dis_target:
    dis_result = dis_result*daily_up
    day_count += 1
    print(f'{day_count}-й день : {dis_result:.2f} км')
print(f'На {day_count}-й день спортсмен достиг результата — не менее {dis_target} км')
