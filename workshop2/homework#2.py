# 1. 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 6782 -> 23
# 0,56 -> 11

# number = input('Введите число: ')
# sum = 0
# number2 = number

# sum = 0
# for i in number:
#     if i != ".":
#     if i.isdigit():
#         sum += int(i)
# print(f'Сумма цифр в числе {number2} = {sum}')

# 1. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1**2, 1**2**3, 1**2**3**4)

# print('\n')

# n = int(input('Введите число N: '))

# print(f'Набор произведений чисел от 1 до {n}:')
# for i in range(1, n+1):
#     sum = 1
#     for j in range(1, i+1):
#         sum *= j
#     print(sum, end=', ')

# print('\n')

# Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
# Как я понял, последовательность должна увеличиваться? 
# Если задаем n = 4, то в формуле n = 1, затем  n = 2 и т.д.?

# print()
# n = int(input('Введите число N: '))
# list = []
# for i in range(0, n):
#     list.append(round((1 + 1/(i+1))**(i+1), 3))

# sum = 0
# for j in range(len(list)):
#     sum += list[j]

# print(f'Спиисок из {n} чисел последовательности (1 + 1/n)**n : ')
# print(list)
# print(f'Сумма элементов в списке: {round(sum, 2)}')
# print()

# 5. Реализуйте алгоритм перемешивания списка.

#вариант1:
import random 

list = [1, 2, 3, 4, 5, 6] 
print(list)
 
random.shuffle(list) 
print(list)

#вариант2:
import random
list = [1, 2, 3, 4, 5, 6] 
print(list)

for i in range(len(list)):
    list[i] = random.choice(list)
print(list)

#вариант3:
import random
list = [1, 2, 3, 4, 5, 6] 
print(list)

temp = None
for i in range((len(list)) // 2):
    temp = list[i]
    list[i] = list[len(list)-(i+1)]
    list[len(list)-(i+1)] = temp
print(list)
