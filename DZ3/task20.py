# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, тоько одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12

t_1 = ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T',
       'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т')
t_2 = ('D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У')
t_3 = ('B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я')
t_4 = ('F', 'H', 'V', 'W', 'Y', 'Й', 'Ы')
t_5 = ('K', 'Ж', 'З', 'Х', 'Ц', 'Ч')
t_8 = ('J', 'X', 'Ш', 'Э', 'Ю')
t_10 = ('Q', 'Z', 'Ф', 'Щ', 'Ъ')

points = {t_1: 1, t_2: 2, t_3: 3, t_4: 4, t_5: 5, t_8: 8, t_10: 10}

word = input('Enter ur  word: ').upper()
letters = set(word)
w_points = 0
for letter in letters:
    if t_1.__contains__(letter):
        w_points += points[t_1]*word.count(letter)
    elif t_2.__contains__(letter):
        w_points += points[t_2]*word.count(letter)
    elif t_3.__contains__(letter):
        w_points += points[t_3]*word.count(letter)
    elif t_4.__contains__(letter):
        w_points += points[t_4]*word.count(letter)
    elif t_5.__contains__(letter):
        w_points += points[t_5]*word.count(letter)
    elif t_8.__contains__(letter):
        w_points += points[t_8]*word.count(letter)
    else:
        w_points += points[t_10]*word.count(letter)
print(w_points)
