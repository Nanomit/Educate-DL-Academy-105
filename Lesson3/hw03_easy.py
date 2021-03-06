import random

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print('Start program 1')

fruit = ["Яблоко", "Банан", "Киви", "Арбуз"]
for i, fruit in enumerate(fruit):
    i = i + 1
    print('{}. {:>6}'.format(i, fruit))



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print("\nStart program 2")

lst1 = [random.randrange(1, 20, 1) for i in range(10)]
lst2 = [random.randrange(1, 20, 1) for i in range(10)]
print('Список 1 = {} \nСписок 2 = {}'.format(lst1, lst2))
for i in lst2:
    if i in lst1:
        lst1.remove(i)
print('Список =', lst1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print("\nStart program 3")

lst1 = [random.randrange(1, 20, 1) for i in range(5)]
print('Список =', lst1)
lst2 = []
for i in lst1:
    if i % 2 == 0:
        lst2.append(i / 4)
    else:
        lst2.append(i * 2)
print(lst2)
