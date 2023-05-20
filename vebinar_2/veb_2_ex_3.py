# lesson 3

number = int(input('Введите номер месяца: '))
d = dict(key1='Winter', key2='Winter', key3='Spring', key4='Spring', key5='Spring', key6='Summer',
key7='Summer', key8='Summer', key9='Autumn', key10='Autumn', key11='Autumn', key12='Winter')
for i in d:
    if 'key'+str(number) == i:
        print (f'Время года - {d.get(i)}')