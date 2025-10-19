# Задачи "Практика 6"
# Задача 6.3
# 3.1)
print("Задача 6 - 3.1")
def number1():
    D = [5, 10, 15, 8, 16, 3, 6, 9, 4, 11]
    n = len(D)
    k1 = 0
    for i in range(n):
        if i % 2 != 0:
            k1 += D[i]

    print(D)
    print(k1)

number1()

# 3.2)
print("Задача 6 - 3.2")
def number2():
    m = [10, 20, 5, 30, 12, 25, 8, 18]
    print("Исходное массив: ", m)

    for i in range(len(m)):
        if m[i] < 15:
            m[i] *= 2

    print("Новый массив: ", m)

number2()


# 8.1)
print("Задача 8.1")
s = [12, 10, 5, 8, 2, 11, 16, 9]
print("Исходный массив: ", s)
summ = sum(s)

k = 1
for n in s:
    k = k * n

print("Сумма: ", summ)
print("Производная: ", k)
print()

# 8.2
print("Задача 8.2")
num = [1.8, 0, 2.9, 3.1, 0, 2.5, 5.6, 0]
srzanch = sum(num) / len(num)
print("Ср. Ариф. (без округления): ", srzanch)

for i in range(len(num)):
    if num[i] == 0:
        num[i] = srzanch

print("Ср. Ариф.: ", round(srzanch, 2))