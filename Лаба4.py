# Задачи "Практика 4"
print("Номер 1")
a1 = int(input("num1: "))
b1 = int(input("num2: "))
if a1 <= b1:
    res = list(range(a1, b1 + 1))
    print(res)
else:
    print("Ошибка!")
print()


print("Номер 2")
a2 = int(input("num1: "))
b2 = int(input("num2: "))
if a2 < b2:
    res1 = list(range(a2, b2 + 1))
    print(res1)
else:
    res2 = list(range(a2, b2 - 1, -1))
    print(res2)
print()


print("Номер 3")
a3 = int(input("num1: "))
b3 = int(input("num2: "))
if a3 > b3:
    for i in range(a3, b3 - 1, -1):
        if i % 2 == 0:
            print(i)
else:
    print("Ошибка!")
print()


print("Номер 5")
n5 = int(input("number: "))
k = 0
for i in range(1, n5 + 1):
    k += i**3
print(k)
print()


print("Номер 7")
n7 = int(input("number: "))
fac = 1
k = 0
for i in range(1, n7 + 1):
    fac *= i
    k += fac
print(k)
