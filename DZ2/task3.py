# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2^k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

import math
n = int(input("N: "))
i = 0
k = 1
while n > math.pow(2, i):
    print(int(math.pow(2, i)), end=' ')
    i += 1
