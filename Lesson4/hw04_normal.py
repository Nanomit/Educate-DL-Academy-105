import random

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print('Start program 1')


def fibonacci(n, m):
    row = [0, 1]
    for i in range(1, m):
        row.append(row[-2] + row[-1])
    return row[n:]


print(fibonacci(5, 20))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print('\nStart program 2')


def sort_to_max(origin_list):
    sort_list = list()
    for num in origin_list:
        i = 0
        while i < len(sort_list) and num > sort_list[i]:
            i += 1
        sort_list.insert(i, num)
    return print(sort_list)


sort_to_max([random.randrange(-20, 20, 1) for i in range(10)])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print('\nStart program 3')


def my_filter(original_list):
    print(original_list)
    lst = []
    for i in original_list:
        if i >= 0:
            lst.append(i)
    return lst


print(my_filter([random.randrange(-20, 20, 1) for n in range(10)]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print('\nStart program 4')

a = [2, 6]
b = [4, 7]
c = [8, 10]
d = [6, 9]


def parallelogram(a1, a2, a3, a4):
    a1a2 = [a2[0] - a1[0], a2[1] - a1[1]]
    a3a4 = [a4[0] - a3[0], a4[1] - a3[1]]
    a1a4 = [a4[0] - a1[0], a4[1] - a1[1]]
    a2a3 = [a3[0] - a2[0], a3[1] - a2[1]]
    if ((a1a2[0] * a3a4[1] - a1a2[1] * a3a4[0]) == 0) and ((a1a4[0] * a2a3[1] - a1a4[1] * a2a3[0]) == 0):
        return print('True')
    else:
        return print('False')


parallelogram(a, b, c, d)
