def my_generate(start=0, stop=30, step=1):
    n = 0
    number = start
    while number <= stop:
        if number % 2 != 0:
            yield number
            n += 1
        number += step
ranger = my_generate(0,30)
cnt = 1
last = 0
print("Первое, третье и пятое значения: ")
for index, value in enumerate(ranger):
    if index == 0 or index == 4:
        print(value)
    last = value
print(last)
