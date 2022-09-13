
# 1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [2, 3, 5, 9, 3,]
# sum = 0
# for i in range(len(list)):
#     if i % 2 == 1:
#         sum += list[i]
# print(sum)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# list = [2, 3, 4, 5, 6]
# result = []
# maxIndex = len(list) - 1

# for i in range(len(list) // 2):
#     result.append(list[i] * list[maxIndex])
#     maxIndex -= 1
# if len(list) % 2 == 1:
#     result.append(list[len(list) // 2]**2)
# print(result)

# 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [1.1, 1.2, 3.1, 5.0, 10.01]
# result = []

# for i in range(len(list)):
#     if i != 0:
#         result.append(round(list[i] % 1, 2))

# print(max(result) - min(result))

# max = result[0]
# min = result[0]
# for j in range(len(result)):
#     if result[j] < min:
#         min = result[j]
#     elif result[j] > max:
#         max = result[j]
# print(f'Разница между {max} и {min} = {max - min}')

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

decimal_number = int(input(f'Введите десятичное число для преобразования в двоичное: '))
origin_decimal_number = decimal_number
binary_number = ''
 
while decimal_number > 0:
    binary_number = str(decimal_number % 2) + binary_number
    decimal_number //= 2
 
print(f'{origin_decimal_number} в двоичной системе исчисления: {binary_number}')