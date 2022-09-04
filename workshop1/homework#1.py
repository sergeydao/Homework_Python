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