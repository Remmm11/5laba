"""
Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу
сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы применимости рекурсивного и
итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и
графической форме в виде отчета по лабораторной работе.

Вариант 13:
F(1) = 1;
F(n) = (n – 1)! – F(n – 2), при n >=2
"""

import time
import matplotlib.pyplot as plt
from math import factorial
import sys

if hasattr(sys, "set_int_max_str_digits"):
    upper_bound = 0
    lower_bound = 4004
    current_limit = sys.get_int_max_str_digits()
    if current_limit == 0 or current_limit > upper_bound:
        sys.set_int_max_str_digits(upper_bound)
    elif current_limit < lower_bound:
        sys.set_int_max_str_digits(lower_bound)
def rec_f(x):
    if x < 2:
        return 1
    else:
        return factorial(x - 1) - rec_f(x - 2)


def iter_f(x):
    fn = [1] * 3
    for i in range(2, x + 1):
        fn[-1] = factorial(i - 1) - fn[0]
        fn[0], fn[1] = fn[1], fn[2]
    return fn[-1]


try:
    k = 1

    n = int(input('Введите натуральное число n, для функции: F(n) = (n – 1)! – F(n – 2): '))
    while n < 1:
        n = int(input('Введите число n > 0. Рассматриваются только натуральные числа: '))

    l = int(input('\nДля какой функции вы хотите выполнить программу? '
                  '( Итерационной = 0 | Рекурсивной = 1 | Для обеих = 2 ): '))
    while l != 0 and l != 1 and l != 2:
        k = int(input('\nПринимаются только значения "0", "1" или "2": '))

    if l == 0:
        if n > 7000:
            k = int(input('\nЧисло n слишком большое. Работа программы может занять существенное время.'
                          ' Хотите получить результат? ( Да = 1 | Нет = 0 ): '))
        while k != 0 and k != 1:
            k = int(input('\nПринимаются только значения "1" или "0": '))

        start = time.time()
        result = iter_f(n)
        end = time.time()
        print(f'\nРезультат (итерация): {result}\nВремя выполнения (итерация): {end - start} cек.')
    elif l == 1:
        start = time.time()
        result = rec_f(n)
        end = time.time()
        print(f'\nРезультат (рекурсия): {result}\nВремя выполнения (рекурсия): {end - start} cек.')
    elif l == 2:
        s = int(input('\nВведите натуральное число s, являющееся шагом в сравнительной таблице и графике: '))
        while s < 1:
            s = int(input('Введите число s больше 0. Шаг не может быть меньше 1: '))
        # Проверка на ожидание
        if n > 7000:
            k = int(input(
                '\nЧисло n слишком большое. Работа программы может занять существенное время.'
                ' Хотите получить результат? ( Да = 1 | Нет = 0 ): '))
        while k != 0 and k != 1:
            k = int(input('\nПринимаются только значения "1" или "0": '))
        # Итерационный подход
        start = time.time()
        result = iter_f(n)
        end = time.time()
        print(f'\nРезультат: {result}\nВремя выполнения (итерация): {end - start} cек.')
        # Рекурсивный подход
        start = time.time()
        result = rec_f(n)
        end = time.time()
        print(f'Время выполнения (рекурсия): {end - start} cек.')
        # Заготовки для таблицы
        rec_times = []
        rec_values = []
        iter_times = []
        iter_values = []
        n_values = list(range(1, n + 1, s))

        for n in n_values:
            start = time.time()
            rec_values.append(rec_f(n))
            end = time.time()
            rec_times.append(end - start)

            start = time.time()
            iter_values.append(iter_f(n))
            end = time.time()
            iter_times.append(end - start)

        table = []
        if n < 40:
            for i, n in enumerate(n_values):
                table.append([n, iter_values[i], rec_values[i], iter_times[i], rec_times[i]])
            # Вывод таблицы
            a = '¯' * 212
            b = '_' * 212
            c = '-' * 212
            print('\nТаблица:')
            print(f'|{a}|')
            print('|{:^24}|{:^46}|{:^46}|{:^46}|{:^46}|'.format('n', 'Значение итерации', 'Значение рекурсии',
                                                                'Время итерации(с)', 'Время рекурсии(с)'))
            print(f'|{c}|')
            for value in table:
                print('|{:^24}|{:^46}|{:^46}|{:^46}|{:^46}|'.format(value[0], value[1], value[2], value[3], value[4]))
            print(f'|{b}|')
        else:
            print('\nИз-за большого значения n значение итерации и рекурсии не помещается в таблицу, поэтому её вывод'
                  ' не целесообразен.')

        print('\nОтчёт:\nИтерационный подход в среднем работает в 2 раза дольше рекурсивного.'
              '\nНо рекурсивный подход перестает работать при n = 1996 и больше.\nТо-есть рекурсивный'
              ' подход будет выгоден при малых значениях n. А итерационный сможет выдать ответ при любом n, но за '
              'большее время.')

        plt.plot(n_values, rec_times, label='Рекурсивная функция.')
        plt.plot(n_values, iter_times, label='Итерационная функция.')
        plt.legend(loc=2)
        plt.xlabel('Значение n')
        plt.ylabel('Время выполнения (c)')
        plt.show()

    print('\nРабота программы завершена.')

except RecursionError:
    print(
        '\nВы превысили относительную максимальную глубину рекурсии. Перезапустите программу и введите число меньше.')