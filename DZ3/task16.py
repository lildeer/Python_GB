# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
n = int(input('Enter N: '))
check = True
while check:
    A = [int(s) for s in input("Input A: ").split()]
    if n == len(A):
        check = False
    else:
        print('Ur input is incorrect, try one more time')
x = int(input('Enter x: '))
print('A contains {} times {}'.format(A.count(x), x))
