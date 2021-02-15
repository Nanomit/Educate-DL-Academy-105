
# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили

print('\nStart program 1')

def convert(km):
    miles = km / 1.609
    print(round(miles, 3))

convert(20)




# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print('\nStart program 2')

def my_round(number, ndigits):
    step = pow(10, int(ndigits))
    num = float(number) * step
    result = int(num)
    remains = num - result
    if remains > 0.6:
        if result > 0:
            result += 1
        elif remains < 0.4:
            result -= 1
    return result / step



print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# либо False (если счастливый и несчастливый соответственно)

print('\nStart program 3')

def lucky_ticket(ticket_number):
    tn_num = str(ticket_number)
    if len(tn_num) != 6:
        return False
    first = 0
    last = 0
    for i in range(3):
        first += int(tn_num[i])
        last += int(tn_num[-i - 1])
    return first == last



print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

