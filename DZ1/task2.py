# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# вообще, эти выражение равны, так как выражение справа - это упрощение (ракскрытие скобок) выражения слева.

for x in range(2):
    for y in range(2):
        for z in range(2):
            val = False
            if not (x or y or z) == (not x and not y and not z):
                val = True
            print(x, y, z, val)
