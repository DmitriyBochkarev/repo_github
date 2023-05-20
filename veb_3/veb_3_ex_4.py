# 4) Программа принимает действительное положительное число x и целое отрицательное число
# y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
# в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
# помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

def my_func (x, y):
    res = x**y
    print (res)
def my_func2 (x, y):
    i = -1
    res = 1/x
    while i > y:
        res = res * (1/x)
        i -= 1
    print (res)
number1 = input("Введите действительное положительное число ")
while True:
    try :
        number1 = int(number1)
        while number1 <= 0:
            number1 = input("Введите действительное положительное число ")
        break
    except:
        if number1.isalpha():
            print ("Введены буквы")
            number1 = input("Введите действительное положительное число ")
        else:
            try:
                number1=int(number2)
                if number1 <= 0:
                    number1 = input("Введите действительное положительное число ")
            except:
                print ("Введены непонятные символы")
                number1 = input("Введите действительное положительное число ")
number2 = input ("Введите целое отрицательное число ")
while True:
    try :
        number2 = int(number2)
        while number2 >= 0:
            number2 = input ("Введите целое отрицательное число ")
        break
    except:
        if number2.isalpha():
            print ("Введены буквы")
            number2 = input ("Введите целое отрицательное число ")
        else:
            try:
                number1=int(number2)
                if number2 >= 0:
                    number2 = input ("Введите целое отрицательное число ")
            except:
                print ("Введены непонятные символы")
                number2 = input("Введите целое отрицательное число ")
my_func(number1, number2)
my_func2 (number1, number2)