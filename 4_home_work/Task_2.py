# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного
# аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

# my_list = ['myata', 'slon', 'dog']
# my_list2 = [1, 2, 3]
#
# def magic(my_list_, my_list2_):
#     my_resul = {my_list2_[i]: my_list_[i] for i in range(len(my_list))}
#     return my_resul
# print(magic(my_list, my_list2))

my_list = {'myata': 1, 'slon': 2, 'dog': 3}

def magic(my_list_):
    my_resul = {my_list.values(): my_list.items() for i in range(len(my_list))}
    return my_resul
print(magic(my_list))
