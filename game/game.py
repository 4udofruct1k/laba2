import random

def user_ch():
    while True:
        try:
            choice = int(input("Введите 1 - камень, 2 - ножницы, 3 - бумага: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")
        except ValueError:
            print("Повторите ввод")

def comp_choice():
    return random.randint(1, 3)

def win(usr_choice, computer_choice):
    if usr_choice == computer_choice:
        return "Ничья!"
    elif (usr_choice == 1 and computer_choice == 2) or \
         (usr_choice == 2 and computer_choice == 3) or \
         (usr_choice == 3 and computer_choice == 1):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

def play_game():
    user_choice = user_ch()
    computer_choice = comp_choice()
    choices = {1: "камень", 2: "ножницы", 3: "бумага"}
    print(f"Компьютер выбрал: {choices[computer_choice]}")
    result = win(user_choice, computer_choice)
    print(result)

play_game()