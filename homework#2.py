# 1. 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 6782 -> 23
# 0,56 -> 11

number = input('Введите число: ')
sum = 0
number2 = number

sum = 0
for i in number:
    # if i != ".":
    if i.isdigit():
        sum += int(i)
print(f'Сумма цифр в числе {number2} = {sum}')