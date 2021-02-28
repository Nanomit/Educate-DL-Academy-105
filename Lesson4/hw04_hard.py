import re
from fractions import Fraction

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

print("\nStart program 1")

s = input('Введите выражение в виде n1 x1/y1 + n2 x2/y2, '
          'дробь должна иметь вид n x/y ,где n - целая часть, x - числитель, у - знаменатель. ')

a, op, b = re.split(r'( [+] | [-] |[*] | [/] )', s)
a = sum([abs(Fraction(x)) for x in a.split()])*(-1 if a[0] == '-' else 1)
b = sum([abs(Fraction(x)) for x in b.split()])*(-1 if b[0] == '-' else 1)
res = eval('a'+op+'b')
x, y = res.numerator, res.denominator
if y == 1:
    print(x)
else:
    n, p = divmod(abs(x), y)
    if n:
        print(f'{-n if x<0 else n} {p}/{y}')
    else:
        print(f'{x}/{y}')

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

print("\nStart program 2")


def select(x):
    mani, time, real_time = list(map(int, x))
    if time > real_time:
        res = mani / time * real_time
    else:
        res = mani + (mani / time * real_time - time) * 2
    return int(res)


with open('Data/workers.txt', encoding='utf-8') as inp, open('Data/hours_of.txt', encoding='utf-8') as time:
    list_norm = inp.read().split('\n')
    list_real = time.read().split('\n')


def name_data(x):

    x = x.split()
    name, mani, time = ' '.join(x[:2]), x[2], x[4]
    return name, [mani, time]


full_data = dict()
for x in list_norm[1:]:
    name, data = name_data(x)
    full_data[name] = data
for i in list_real[1:]:
    i = i.split()
    full_data[' '.join(i[:2])].append(i[-1])

with open('Data/result.txt', 'w', encoding='utf-8') as out:
    out.write('Имя Фамилия  Зарплата  Норма_часов  Отработано  К выдаче\n')
    for name in full_data:
        out.write('{}  {}  {}  {}   {}\n'.format(name, *(full_data[name]), select(full_data[name])))
print("Результат записан в файл result.txt")

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
