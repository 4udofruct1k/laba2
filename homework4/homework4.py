import random

krats = []
def krat(number, func):

    while True:
        try:
            x = int(input("Введите цифру X: "))
            if 0 <= x <= 9:
                break
            else:
                print("Введите цифру, а не число.")
        except ValueError:
            print("Пожалуйста, введите цифру.")
    for num in number:
        if num % x == 0:
            func(num)

numbers = [random.randint(0, 200) for i in range(15)]
print("Сгенерированные числа:", numbers)
krat(numbers, lambda num: krats.append(num))
if krats:
    print("Числа, кратные X: ")
    for i in krats:
        print(i)
else:
    print("Нет чисел, кратных X")
