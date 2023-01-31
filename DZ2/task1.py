# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input("Number of coins "))

coins = [int(s) for s in input("Input u coins: ").split()]
coins0 = 0
coins1 = 0
for coin in coins:
    if coin == 0:
        coins0 += 1
    else:
        coins1 += 1
if coins0 > coins1:
    print(coins1)
else:
    print(coins0)
