import math
__author__ = 'Филоненко Константин'

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

# TODO: код пишем тут...
print('Start program 1')
name = input('Введите ваше имя ')
age = int(input('Введит ваш возраст '))

a = 18
b = age - a
if b > 0:
    if b == 1:
       print(name, 'на', b, 'год больше 18')
    elif b < 5:
           print(name, 'на', b, 'года больше 18')
    else:
           print(name, 'на', b, 'лет больше 18')
else:
     b = -b
     if b == 1:
        print(name, 'на', b, 'год меньше 18')
     elif b < 5:
            print(name, 'на', b, 'года меньше 18')
     else:
         print(name, 'на', b, 'лет меньше 18')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# TODO: код пишем тут...

print('Start program 2')
x = input('Введите переменную а ')
y = input('Введите переменную b ')

z = x
x = y
print('a =', x, 'b =', z)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# TODO: код пишем тут...

print('Start program 3')

a = float(input("Введите число а "))
b = float(input("Введите чило b "))
c = float(input("Введите число c "))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    print("X1 = ", round(x1,3), " X2 = ", round(x2,3))
elif D == 0:
    x1 = -(b/(2*a))
    print("X1 = X2= ", x1)
else:
    print("Нет корней")
