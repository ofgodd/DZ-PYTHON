# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

coin = int(input("Число монеток: "))
Coin_eagle = 0
Coin_tails = 0

for i in range(coin):
    Coin_enter = int(input("Введите сторону монет, где 1 решка 0 орел: "))
    if Coin_enter == 1:
        Coin_tails += 1
    else:
        Coin_eagle += 1

if Coin_tails > Coin_eagle:
    print(f"Необходимо перевернуть монету орел {Coin_eagle}")
else:
    print(f"Необходимо перевернуть монету решка {Coin_tails}")
