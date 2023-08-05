# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if. Попробуйте разные значения e и n.
e, n = int(input("Введите e: ")), int(input("Введите n: "))
count = 0
summ = 0
while count < n:
    if count % 2 == 0 and count % e !=0:
        summ += count
    count += 1
print(summ)
