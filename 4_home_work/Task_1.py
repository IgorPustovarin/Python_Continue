# Напишите функцию для транспонирования матрицы
#
# string_one = [1, 4, 6]
# string_two = [3, 5, 9]
# string_three = [2, 7, 0]
# print(f'{string_one} \n{string_two} \n{string_three}\n')
#
# def transposition (string_one_, string_two_, string_three_):
#     for i in range(len(string_one)):
#         string_new1 = [string_one_[i], string_two_[i], string_three_[i]]
#         print(string_new1)
#     return string_new1
# transposition(string_one, string_two, string_three) Это не правильно решение

# Это правильное решение (два варианта)
my_matrix = [[1, 2, 3], [4, 5, 6]]
def trans_for(matrix: list[list[int]]) -> list[list[int]]:
    temp = []
    for i in range(len(matrix[0])):
        temp.append([])
        for j in range(len(matrix)):
            temp[i].append(matrix[j][i])
        return temp
def trans_zip(matrix: list[list[int]]) -> list[list[int]]:
    return list(zip(*matrix))

print(trans_for(my_matrix))
print(trans_zip(my_matrix))

