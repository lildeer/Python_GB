# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

x1, y1 = [int(s) for s in input("Input x1 and y1: ").split()]
x2, y2 = [int(s) for s in input("Input x2 and y2: ").split()]
dist = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))
print(f'Distance is {dist:.2f}')