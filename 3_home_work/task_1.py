# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
my_list = [4, 3, 3, 3, 5, 5, 6, 7, 4, 1]
print(my_list)
new_list = []
for i in my_list:
    if i not in new_list:
        if my_list.count(i) > 1:
            new_list.append(i)
print(new_list)

