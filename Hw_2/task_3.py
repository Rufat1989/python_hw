# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число N: '))
print('Все целые степени двойки: ')
i = 1
while 2 ** i <= n:
        print(2 ** i)
        i += 1