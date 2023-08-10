# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

num_1 = str(input("Введи первую дробь: "))
num_2 = str(input("Введи вторую дробь "))

chislit_1: int = int(num_1.split('/')[0])
znam_1: int = int(num_1.split('/')[1])
chislit_2: int = int(num_2.split('/')[0])
znam_2: int = int(num_2.split('/')[1])
print("Сумма ")

# print(f"{chislit_1}, {znam_1}, {chislit_2}, {znam_2}\n")
if znam_1 == znam_2:
    print(f"{chislit_1 + chislit_2}/{znam_1}")
elif znam_1 % znam_2 == 0:
    print(f"{chislit_1 + chislit_2*(znam_1/znam_2)}/{znam_1}")
elif znam_2 % znam_1 == 0:
    print(f"{chislit_1*(znam_2/znam_1) + chislit_2}/{znam_2}")
else:
    print(f"{chislit_1 * znam_2 + chislit_2 * znam_1} / {znam_1 * znam_2}")

print("Произведение ")
print(f"{chislit_1 * chislit_2}/{znam_1 * znam_2}")


