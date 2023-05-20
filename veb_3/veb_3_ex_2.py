# 2) Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Реализовать вывод данных о
# пользователе одной строкой.

def user ():
    name = input("Введите имя ")
    surname = input("Введите фамилию ")
    year = input("Введите год рождения ")
    city = input("Введите город проживания ")
    email = input("Введите email ")
    tel = input("Введите номер телефона ")
    txt_list = [name, surname, city]
    numbers_list = [year, tel]
    for i in txt_list:
        if i.isalpha():
            break
        else:
            if txt_list.index(i) == 0:
                print('Данные в поле ИМЯ введены неверно.')
                name = input("Введите имя ")
            elif txt_list.index(i) == 1:
                print('Данные в поле ФАМИЛИЯ введены неверно.')
                surname = input("Введите фамилию ")
            else:
                print('Данные в поле ГОРОД введены неверно.')
                city = input("Введите город проживания ")
    for i in numbers_list:
        try:
            i = int(i)
            break
        except:
            if numbers_list.index(i) == 0:
                print('Данные в поле ГОД введены неверно.')
                year = input("Введите год рождения ")
            else:
                print('Данные в поле ТЕЛЕФОН введены неверно.')
                tel = input("Введите номер телефона ")
    print (f'Пользователь {name} {surname} {year} года рождения, проживающий в городе {city}, электронная почта {email}, телефон {tel}')
user ()