def creat_array():
    array = []
    for i in range(3):
        array_1 = []
        for j in range(3):
            array_1.append('-')
        array.append(array_1)
    return array


def print_array(array):
    for i in range(3):
        print("  ".join(array[i]))


def chek_win(array):
    win = '-'
    result_diagonal = ''
    for i in range(3):
        result_line = ''
        result_row = ''
        for j in range(3):
            result_line += array[i][j]          #Проверка строки
            result_row += array[j][i]               #Проверка столбца
            if i == j or i + j == 2:                    #Проверка диагонали
                result_diagonal += array[i][j]
        if result_line == 'XXX' or result_row == 'XXX' or result_diagonal == 'XXX':
            win = 'X'
        elif result_line == 'OOO' or result_row == 'OOO' or result_diagonal == 'OOO':
            win = 'O'

    return win


table = creat_array()
char = 'X'
while True:
    print_array(table)
    row = int(input('Введите столбец : '))
    line = int(input('Введите строку : '))
    table[line - 1][row - 1] = char
    if char == 'X':
        char = 'O'
    else:
        char = 'X'
    if chek_win(table) == 'O' or chek_win(table) == 'X':
        print_array(table)
        print(f'Победили {chek_win(table)}')
        break

# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;


# str_user = input('Введите выражение для подсчета : ').replace(' ', '')
# list_str = []
#
#
# # Зачистка уже подсчитаных элементов из списка
# def clearing(array, i, result):
#     array.pop(i + 1)
#     array.pop(i)
#     array.pop(i - 1)
#     array.insert(i - 1, result)
#     return
#
#
# # Проверка на - первого элемента выражения
# if str_user[0] == '-':
#     str_user = str_user[1:]
#     num = '-'
# else:
#     num = ''
#
# # Перевод строки в список с учетом двухзначных чисел
# for k in str_user:
#     if k.isdigit():
#         num += k
#     else:
#         list_str.append(int(num))
#         num = ''
#     if not k.isdigit():
#         list_str.append(k)
# list_str.append(int(num))
# print(list_str)
#
# # Первое действие * /
# while '*' in list_str or '/' in list_str:
#     for i, j in enumerate(list_str):
#         if j == '*':
#             result = list_str[i - 1] * list_str[i + 1]
#             clearing(list_str, i, result)
#             break
#
#         elif j == '/':
#             result = list_str[i - 1] / list_str[i + 1]
#             clearing(list_str, i, result)
#             break
#
# # Второе действие - +
# while '-' in list_str or '+' in list_str:
#     for i, j in enumerate(list_str):
#         if j == '-':
#             result = list_str[i - 1] - list_str[i + 1]
#             clearing(list_str, i, result)
#             break
#
#         elif j == '+':
#             result = list_str[i - 1] + list_str[i + 1]
#             clearing(list_str, i, result)
#             break
# print(list_str)
