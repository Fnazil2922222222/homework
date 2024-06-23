first = int(input('Введите число A = '))
second = int(input('Введите число B = '))
third = int(input('Введите число C = '))
if (first==second) and (second==third) and (first==third) :
    print('Количество одинаковых чисел: ', 3)
elif (first==second) or (second==third) or (first==third) :
    print('Количество одинаковых чисел: ', 2)
else:
    print('Количество одинаковых чисел: ', 0)