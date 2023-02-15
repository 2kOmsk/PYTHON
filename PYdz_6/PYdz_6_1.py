def calc_salary(hours, rate, bonus):
    return hours * hour_rate + bonus_rate

if __name__ == "__main__":
    hours = int(input("Введите количество отработанных часов: "))
    hour_rate = int(input("Введите ставку в час: "))
    bonus_rate = int(input("Введите премию: "))
    salary = calc_salary(hours, rate, bonus)
    print("Заработная плата сотрудника: {}".format(salary))
