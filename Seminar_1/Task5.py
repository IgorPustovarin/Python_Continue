 # Нарисовать в консоли Ёлку спросив у пользователя количество рядов.
 # Пример результата:
 # Сколько рядов у Ёлки? 5
 #     *
 #    ***
 #   *****
 #  *******
 # *********
# num = int(input('Сколько рядов у ёлки? ')) #ПЕРВЫЙ ВАРИАНТ РЕШЕНИЯ
# # chr_tree_width = num * 2 -1
# stars = 1
# for i in range(num):
#     print(f"{' ' * (num - 1)}{'*' * stars}")
#     stars += 2
#     num -= 1

num = int(input('Сколько рядов у ёлки? ')) #ВТОРОЙ ВАРИАНТ РЕШЕНИЯ, ЧЕРЕЗ ФОРМАТИРОВАНИЕ СТРОКИ

for i in range(num):
    print(f'{"*"*(2*i+1):ю^{(num*2-1)}}') #там где буква "Ю" вводим символ чем заполнять, можем пробелами
