# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного
# аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

# my_list = ['myata', 'slon', 'dog']
# my_list2 = [1, 2, 3]
#
# def magic(my_list_, my_list2_):
#     my_resul = {my_list2_[i]: my_list_[i] for i in range(len(my_list))}
#     return my_resul
# print(magic(my_list, my_list2))
#
# my_list = {'myata': 1, 'slon': 2, 'dog': 3}
#
# def magic(my_list_):
#     my_resul = {my_list.values(): my_list.items() for i in range(len(my_list))}
#     return my_resul
# print(magic(my_list)) Это не правильное решение

# Это правильное решение (два варианта)
my_dict = {1: 'one', 2: ['two'], '3': ('three',)}

def inverse_try(**kwargs) -> dict:
    new_dict = {}
    for key, value in kwargs.items():
        try:
            new_dict[value] = key
        except:
            new_dict[str(value)] = key
        return new_dict

def inverse_instance(**kwargs) -> dict:
    new_dict = {}
    for key, value in kwargs.items():
        if not isinstance(value, list | set | dict):
            new_dict[value] = key
        else:
            new_dict[str(value)] = key
        return new_dict

def inverse_hash(**kwargs) -> dict:
    new_dict = {}
    for key, value in kwargs.items():
        if value.__hashble__():
            new_dict[value] = key
        else:
            new_dict[str(value)] = key
        return new_dict

print(inverse_try(one = 1, two=['2'], three=(3,)))
print(inverse_instance(one = 1, two=['2'], three=(3,)))

