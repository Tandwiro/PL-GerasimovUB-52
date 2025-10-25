# Задачи "Практика 7"
# Задача 7.1
import math

# Задача 3.1
print("Задача 3.1")
a1 = float(input("1й катет первого треугольника: "))
b1 = float(input("2й катет первого треугольника: "))

a2 = float(input("1й катет второго треугольника: "))
b2 = float(input("2й катет второго треугольника: "))

def hypot(a,b):
    hyp = math.sqrt((a**2) + (b**2))
    return hyp

hyp1 = hypot(a1,b1)
hyp2 = hypot(a2,b2)
print(hyp1)
print(hyp2)

if hyp1 > hyp2:
    print("Гипотенуза первого треугольника БОЛЬШЕ")
    print("Гипотенуза второго треугольника МЕНЬШЕ")
elif hyp1 < hyp2:
    print("Гипотенуза первого треугольника МЕНЬШЕ")
    print("Гипотенуза второго треугольника БОЛЬШЕ")
else:
    print("Гипотенузы РАВНЫ")


# Задача 7.2
print("Задача 3.2")
def sorting_letters(text):
    letters = text.split()
    res_let = []
    for letter in letters:
        letters = list(letter)
        letters.sort()
        sorted_letter = ' '.join(letters)
        res_let.append(sorted_letter)
    result = ''.join(res_let)
    return result

n = input("Ввод: ")
sort_n = sorting_letters(n)
print(n)
print(sort_n)


# Задача 7.3
print("Задача 8.1")
n = 100
for i in range(1, n + 1):
    num = i
    flag = True

    while num > 0:
        digit = num % 10
        if digit == 0 or i % digit != 0:
            flag = False
            break
        num //= 10
    if flag:
        print(i, end='')

print("Задача 8.2")
def zam(x):
    tmp = X[0]
    x[0] = X[len(X)-1]
    X[len(X)-1]=tmp


    
