# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.

number1 = input("Введите первое число ")
number2 = input("Введите второе число ")
def two_numbers (a, b):
    while True:
        try:
            a = int (a)
            b = int (b)
            break
        except:
            print("Нужно ввести числа!")
            a = input("Введите первое число ")
            b = input("Введите второе число ")
    while True:
        try:
            res = a / b
            break
        except:
            print("Делить на ноль нельзя")
            b = int(input("Введите второе число "))
    print(res)
two_numbers(number1, number2)