# Задачи "Практика 3"
# Задача 3 1.2
print("Задание 3.1")
n = int(input("Введите двузначное число: "))

# if n == 11 or n == 22 or n == 33 or n == 44 or n == 55 or n == 66 or n == 77 or n == 88 or n == 99:
#     print("ДА!")
# else:
#     print("Нет!")

# или
n1 = n // 10
n2 = n % 10

if n1 == n2:
    print("ДА!")
else:
    print("Нет!")


# Задача 3 2.3
print("Задание 2.3")
a = int(input("num1: "))
b = int(input("num2: "))

if a < b:
    C = a + b
elif a > b or a > 3:
    C = b**2 - b
else:
    C = b**2 - 1

print(C)


# Задача 3 3.3
print("Задание 3.3")
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ch = []
nch = []
for i in n:
    if i % 2 == 0:
        ch.append(i)
    else:
        nch.append(i)
print("Чётные: ", ch)
print("Нечётные: ", nch)