# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

from translate import Translator
translator= Translator(to_lang="Russian")
i = 0
with open("numbers.txt", "r") as my_f:
    for line in my_f:
        i +=1
        translation = translator.translate(line[:-6])
        with open("new.txt", 'a') as new_f:
            new_f.write(translation + " - " + str(i) + "\n")