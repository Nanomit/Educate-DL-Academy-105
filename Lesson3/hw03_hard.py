import addition
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y

print('Start program 1')

equation = 'y = -12x + 11111140.2121'
x = 2.5

a1 = equation.find('x')
a2 = equation.find('=') + 2
a = float(equation[a2:a1])

if (equation[a1 + 2]) == '-':
    sign = -1
else:
    sign = 1

b = float(equation[a1 + 4:]) * sign

y = a * x + b
print(y)


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'


print('\nStart program 2')

date = input('Введите дату в виде dd.mm.yyyy ')
if not len(date) == 10:
    print('Дата введена некорректно')
else:
    if not date[2] == '.' or not date[5] == '.':
        print('Разделители должны быть точками')
    else:
        date2 = date.split('.')
        if not len(date2[0]) == 2 or not len(date2[1]) == 2 or not len(date2[2]) == 4:
            print('Дата введена некорректно')
        elif not addition.check_int_date(date2) == True:
            print('В введенных данных присутсвуют некорректные символы')
        else:
            day = int(date2[0])
            month = int(date2[1])
            year = int(date2[2])
            if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
                print('В этом месяце не может быть больше 31 дня')
            elif month in [2, 4, 6, 9, 11] and day > 30:
                print('В этом месяце не может быть больше 30 дней')
            elif month > 12:
                print('В году не может быть больше 12 месяцев')
            elif year < 1:
                print('Такого года не существует')
            elif day < 1:
                print('Некорректно указан день')
            else:
                print('Дата - {} была введена правильно'.format(date))

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
print('\nStart program 3')

room_num = int(input('Введите номер комнаты: '))
tower = []
a = 0
b = 0
f = 0
d = 0

while a < room_num:
    b += 1
    block = []
    for i in range(b):
        f += 1
        floor = []
        for d in range(b):
            a += 1
            floor.append(a)
            if a == room_num:
                print('Номер комнаты:', room_num, '\nЭтаж:', f, 'Очередность комнаты:', d + 1)
        block.append(floor)
    tower.append(block)


