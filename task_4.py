# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

amount = int(input('Введите количество сделанных журавликов: '))
if amount % 6 != 0:
    print("Введенное число не удовлетворяет условиям задачи")
else:
    print("Сделано журавликов: ")
    print(f'Петей: {int(amount / 6)}')
    print(f'Катей: {int(amount / 3 * 2)}')
    print(f'Сережей: {int(amount / 6)}')