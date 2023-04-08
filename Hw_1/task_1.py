# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input('Введите трехзначное число: '))

number_1 = a%10
number_2 = a//10%10
number_3 = a//100

sum = number_1 + number_2 + number_3

print(f"{a} -> {sum} ({number_1}, {number_2}, {number_3})"  )
