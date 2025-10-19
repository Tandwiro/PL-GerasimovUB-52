# Задачи "Практика 4"
# Задача 4.3
print("Номер 4 - 3.1")
a = int(input("num1: "))
b = int(input("num2: "))

if a <= b:
    res = list(range(a, b + 1))
    print(res)
else:
    print("ERROR!!!")
print()

# Задача 4 - 3.2
print("Номер 4.2")
a = int(input("num1: "))
b = int(input("num2: "))
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)
print()

# Задача 4 - 3.3
print("Номер 4.3")
a = int(input("num1: "))
b = int(input("num2: "))
if a > b:
    for i in range(a, b - 1, -1):
        if i % 2 == 0:
            print(i)
else:
    print("ERROR!!!")
print()