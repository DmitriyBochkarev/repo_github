# 5) Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.
import random
sum=0
with open("text5.txt", "w") as f:
    for i in range (10):
        number = random.randint(0, 100)
        f.write(str(number) + " ")
        sum += number
print (sum)