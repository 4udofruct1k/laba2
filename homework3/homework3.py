from datetime import datetime
def calc_Age():
    while True:
        datebirthstr = input("Введите дату рождения (дд/мм/гггг): ")
        try:
            datebirth = datetime.strptime(datebirthstr, "%d/%m/%Y")
            break
        except ValueError:
            print("Неверный формат даты. Пожалуйста, введите дату в формате дд/мм/гггг.")
    today = datetime.now()
    age = today.year - datebirth.year
    if (today.month, today.day) < (datebirth.month, datebirth.day):
        age -= 1
    print("Ваш возраст: {age} лет")
calc_Age()
