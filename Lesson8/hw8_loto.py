"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
Если цифра есть на карточке - она зачеркивается и игра продолжается.
Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
Если цифра есть на карточке - игрок проигрывает и игра завершается.
Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random


class Card:
    def __init__(self, name):
        bags = [i for i in range(1, 91)]
        self.card = [__class__.gen_str(bags), __class__.gen_str(bags), __class__.gen_str(bags)]
        self.name = name
        self.drop_keg = 15

    @staticmethod
    def gen_str(bags):
        string = ['' for _ in range(9)]
        for i in range(8, 3, -1):
            digit = random.randint(0, i)
            while string[digit] != '':
                digit += 1
            string[digit] = bags.pop(random.randint(0, len(bags) - 1))
        return string

    def __str__(self):
        rez = '{:-^26}\n'.format(self.name)
        for i in range(3):
            rez += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}' \
                       .format(*self.card[i]) + '\n'
        return rez + '-' * 26


comp = Card(' Карточка компьютера ')
player = Card(' Карточка игрока ')
bag = [i for i in range(1, 91)]

while True:
    if len(bag) < 1:
        print('Бочёнки в мешке закончились. Результат:\n'
              'у компьютера осталось {} чисел,\n'
              'у игрока осталось {} чисел.'
              .format(comp.drop_keg, player.drop_keg))
        break

    keg = bag.pop(random.randint(0, len(bag) - 1))

    print('\nНовый бочонок: {} \n{} \n{} \n{} \n{}'.format(keg, '*' * 26, player, comp, '*' * 26))

    reply = input('\nЗачеркнуть цифру? \nда - y | нет - n | выход - q ')

    while len(reply) == 0 or reply not in 'ynq':
        print('\nОтвет не распознан.\n')
        print('\nНовый бочонок: {} \n{} \n{} \n{} \n{}'.format(keg, '*' * 26, player, comp, '*' * 26))

        reply = input('\nЗачеркнуть цифру? \nда - y | нет - n | выход - q ')

    if reply == 'q':
        print('\n{0} Игра завершена. {0}'.format('*' * 5))
        break

    elif reply == 'y':
        check = False
        for i in range(3):
            if keg in player.card[i]:
                check = True
                player.card[i][player.card[i].index(keg)] = 'X'
                player.drop_keg -= 1
            if keg in comp.card[i]:
                comp.card[i][comp.card[i].index(keg)] = 'X'
                comp.drop_keg -= 1

        if check:
            if player.drop_keg < 1:
                print('{0} Вы Выиграли! {0}'.format('*' * 5))
                break
            elif comp.drop_keg < 1:
                print('{0} Компьютер Выиграл! {0}'.format('*' * 5))
                break

        else:
            print('{0} Игра окончена! Такого числа нет на вашей карточке! {0}'.format('*' * 5))
            break

    elif reply == 'n':
        check = False
        for i in range(3):
            if keg in player.card[i]:
                print('{0} Игра окончена! Такое число есть на вашей карточке! {0}'.format('*' * 5))
                check = True
                break

            if keg in comp.card[i]:
                comp.card[i][comp.card[i].index(keg)] = 'X'
                comp.drop_keg -= 1

        if check:
            break

        if player.drop_keg < 1:
            print('{0} Вы Выиграли! {0}'.format('*' * 5))
            break

        elif comp.drop_keg < 1:
            print('{0} Компьютер Выиграл! {0}'.format('*' * 5))
            break
