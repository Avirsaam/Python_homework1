# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*

number = input('Введите трехзначное число ')

if len(number) != 3 or number.isdigit() == False:
    print("Вы ввели не трехзначное число")
else:
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    print('Сумма цифр введенного числа ', sum)
