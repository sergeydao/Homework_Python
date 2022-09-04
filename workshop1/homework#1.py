# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
#     *Пример:*
#     6 -> да
#     7 -> да
#     1 -> нет

# Вариант №1

day = int(input('Введите число от 1 до 7: '))

if day == 1:
    print('Понедельник')
elif day == 2:
    print('Вторниик')
elif day == 3:
    print('Среда')
elif day == 4:
    print('Четверг')
elif day == 5:
    print('Пятница')
elif day == 6:
    print('Суббота')
elif day == 7:
    print('Воскресенье')

if day == 6 or day == 7:
    print('Ура, выходной!')
else:
    print('Увы, идем на работу...')


# Вариант с функцией:

def Function(day):
    if day == 1:
        print('Понедельник')
    elif day == 2:
        print('Вторниик')
    elif day == 3:
        print('Среда')
    elif day == 4:
        print('Четверг')
    elif day == 5:
        print('Пятница')
    elif day == 6:
        print('Суббота')
    elif day == 7:
        print('Воскресенье')

    if day == 6 or day == 7:
        print('Ура, выходной!')
    else:
        print('Увы, идем на работу...')

day = int(input('Введите число от 1 до 7: '))
print(Function(day))

# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input('Введите координаты точки x: '))
y = int(input('Введите координаты точки y: '))

if x > 0 and y > 0:
    print('Точка находится в первой четверти')
elif x < 0 and y > 0:
    print('Точка находится во второй четверти')
elif x < 0 and y < 0:
    print('Точка находится в третьей четверти')
elif x > 0 and y < 0:
    print('Точка находится в четвертой четверти')


# 3. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти от 1 до 4: '))


if number == 1:
    print('Диапазон 1 четверти: \n0 < x < infinity \n0 < y < infinity')
elif number == 2:
    print('Диапазон 2 четверти: \n-infinity < x < 0 \n0 < y < infinity')
elif number == 3:
    print('Диапазон 3 четверти: \n-infinity < x < 0 \n-infinity < y < 0')
elif number == 4:
    print('Диапазон 4 четверти: \n0 < x < infinity \n-infinity < y < 0')


# 4. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

ax = int(input('Введите координаты AX: '))
ay = int(input('Введите координаты AY: '))
bx = int(input('Введите координаты BX: '))
by = int(input('Введите координаты BY: '))

import math
print('Расстояние между точками A и B в 2D пространстве: ')
print(round(math.sqrt(((bx - ax)**2) + ((by - ay)**2)), 2))

# 5. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def ComparePredicatesXYZ():
    x = int(input('Введите значение Х: '))
    y = int(input('Введите значение Y: '))
    z = int(input('Введите значение Z: '))

    firstPart = not (x or y or z)
    secondPart = not x and not y and not z
    result = firstPart == secondPart
    if result == True:
        print(f"Утверждение истинно")
    else:
        print(f"Утверждение ложно")
   
print(ComparePredicatesXYZ())