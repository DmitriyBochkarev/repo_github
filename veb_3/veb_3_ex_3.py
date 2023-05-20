# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

import random
def my_func ():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    number3 = random.randint(1, 100)
    print (number3, number2, number1)
    if number3 < number2 and number3 < number1:
        res = number2 + number1
    elif number2 < number1 and number2 < number3:
        res = number1 + number3
    else:
        res = number2 + number3
    print (res)
my_func()
