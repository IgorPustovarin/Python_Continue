# Выведите в консоль таблицу умножения от 2*2 до 9*10 как на школьной тетрадке.
for j in range(2, 11): #ПЕРВЫЙ ВАРИАНТ
    for i in range(2, 6):
        print(f'{i:^3} X {j:^3} = {j * i:^3}', end='\t\t')
    print()
print()
for j in range(2, 11):
    for i in range(6, 10):
        print(f'{i:^3} X {j:^3} = {j * i:^3}', end='\t\t')
    print()

# for k in [0, 1]: #ВТОРОЙ ВАРИАНТ
#     for j in range(2, 11):
#     row = []
# for i in range(2 + k * 4, 6 + k * 4):
#     row.append(f'{i:^3} X {j:^3} = {j * i:^3}')
# print('\t\t\t'.join(row))
# print('\n')
