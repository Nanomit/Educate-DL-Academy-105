import os
import shutil

# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
if __name__ == '__main__':
    print('Start program 1')


def avg(x, y):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (x * y) ** 0.5


if __name__ == '__main__':
    while True:
        try:
            a = float(input("a = "))
            b = float(input("b = "))
            break
        except ValueError:
            print("Вы ввели не число")
            continue

if __name__ == '__main__':
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

if __name__ == '__main__':
    print('\nStart program 2')


def make(name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print('{} - уже существует'.format(name))


def remove(name):
    try:
        os.removedirs(name)
    except FileNotFoundError:
        print('{} - папки не существует'.format(name))


if __name__ == '__main__':
    def start():
        answer = ''
        quantity_dirs = range(1, 10)
        while answer != '3':
            answer = input('Выберите пункт меню:\n'
                           '1. Создать папки dir_1 - dir_9\n'
                           '2. Удалить папки dir_1 - dir_9\n'
                           '3. Выход\n'
                           'Выбор: ')
            if answer == '1':
                for i in quantity_dirs:
                    i = str(i)
                    make('dir_' + i)
            elif answer == '2':
                for i in quantity_dirs:
                    i = str(i)
                    remove('dir_' + i)
            elif answer != ('1', '2', '3'):
                print('Вы сделали не верный выбор!')
            elif answer == '3':
                break

if __name__ == '__main__':
    start()

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
if __name__ == '__main__':
    print('\nStart program 3')


def lst(path):
    list_dir = [dir for dir in os.listdir(path) if os.path.isdir(dir)]
    list_dir.sort()
    print(*list_dir)


if __name__ == '__main__':
    path = os.getcwd()
    lst(path)

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

if __name__ == '__main__':
    print('\nStart program 3')


def file_copy():
    name_file = os.path.realpath(__file__)
    new_file = name_file + '.copy'
    if not os.path.isfile(new_file) == True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'


if __name__ == '__main__':
    print(file_copy())
