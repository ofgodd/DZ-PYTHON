# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите число "))
count = 1
while count < N:
    print(count, end=" ")
    count = count*2
    

