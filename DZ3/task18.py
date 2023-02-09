# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('Enter N: '))
check = True
while check:
    A = [int(s) for s in input("Input A: ").split()]
    if n == len(A):
        check = False
    else:
        print('Ur input is incorrect, try one more time')
x = int(input('Enter x: '))

# найдем по минимальной разнице с x
diff_min = abs(A[0]-x)
i_min = 0

for i in range(1, len(A)):
    if abs(A[i] - x) < diff_min:
        diff_min = abs(A[i] - x)
        i_min = i

print(A[i_min])
