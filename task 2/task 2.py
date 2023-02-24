# Найдите сумму цифр трехзначного числа.

n = int(input("Введите трехзначное число "))
sum1 = n%10
n = int(n/10)
sum2 = n%10
n = int(n/10)
sum3 = n%10
Sum = sum1+sum2+sum3
print(Sum)
 