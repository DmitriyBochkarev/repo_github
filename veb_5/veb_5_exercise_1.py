# 1) Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

my_f = open("text.txt", "x")
string = input("Введите текст для записи в файл text.txt ")
my_f.write(f"{string}\n")
while string != "":
    string = input()
    my_f.write(f"{string}\n")
my_f.close()