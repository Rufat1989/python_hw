# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

ticket_num = int(input('Введите шестизначный номер билета: '))

a1 = int(ticket_num/100000)
a2 = int(ticket_num%100000/10000)
a3 = int(ticket_num%10000/1000)
a4 = int(ticket_num%1000/100)
a5 = int(ticket_num%100/10)
a6 = int(ticket_num%10)

if (a1 + a2 + a3) == (a4 + a5 + a6):
    print(f'{ticket_num} -> yes')
else:
    print(f'{ticket_num} -> no')
