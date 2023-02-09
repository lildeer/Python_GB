# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

bush_num = int(input('Enter number of bushes: '))
check = True

while check:
    berries = [int(s) for s in input("Input number of berries: ").split()]
    if bush_num == len(berries):
        check = False
    else:
        print('Ur input is incorrect, try one more time')


max_berries = berries[bush_num-2] + berries[bush_num-1] + berries[0]

t_berries = berries[bush_num-1] + berries[0] + berries[1]

if t_berries > max_berries:
    max_berries = t_berries


for bush in range(1, bush_num-1):
    t_berries = t_berries - berries[bush-2] + berries[bush+1]

    if (t_berries > max_berries):
        max_berries = t_berries

print(max_berries)
