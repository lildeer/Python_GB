# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n, m = [int(s) for s in input("Input n and m: ").split()]
check = True

while check:
    A1 = [int(s) for s in input("Input A1: ").split()]
    if n == len(A1):
        check = False
    else:
        print('Ur input is incorrect, try one more time')

while not check:
    A2 = [int(s) for s in input("Input A2: ").split()]
    if m == len(A2):
        check = True
    else:
        print('Ur input is incorrect, try one more time')

A1 = set(A1)
A2 = set(A2)
inter = list(A1.intersection(A2))
inter.sort()
print(*inter)
