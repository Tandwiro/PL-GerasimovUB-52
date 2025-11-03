# Практика 7
import math

print("Задача 3.1")
# a1 = float(input("1й катет первого треугольника: "))
# b1 = float(input("2й катет первого треугольника: "))
# a2 = float(input("1й катет второго треугольника: "))
# b2 = float(input("2й катет второго треугольника: "))
a1 = 10
b1 = 15
a2 = 13
b2 = 18

def hyp(a,b):
    h = math.sqrt((a**2) + (b**2))
    return h

h1 = hyp(a1,b1)
h2 = hyp(a2,b2)
print(h1)
print(h2)

if h1 > h2:
    print("Гипотенуза первого треугольника БОЛЬШЕ")
    print("Гипотенуза второго треугольника МЕНЬШЕ")
elif h1 < h2:
    print("Гипотенуза первого треугольника МЕНЬШЕ")
    print("Гипотенуза второго треугольника БОЛЬШЕ")
else:
    print("Гипотенузы РАВНЫ")
print()

print("Номер 3.2")
# n = input()
n = "Python"
s = n.split()
sort = []

for i in s:
    sort1 = sorted(i)
    sort2 = ''.join(sort1)
    sort.append(sort2)

res = ' '.join(sort)
print(res)
print()


print("Номер 8.1")
n = 100
for i in range(1, n + 1):
    num = i
    flag = True

    while num > 0:
        d = num % 10
        if d == 0 or i % d != 0:
            flag = False
            break
        num //= 10
    if flag:
        print(i, end='')
print()
print()

print("Номер 8.2")
def element(mas):
    if len(mas) > 1:
        first = mas[0]
        last = mas[-1]
        mas[0] = last
        mas[-1] = first
m = int(input("Длина массива: "))
A = []
for i in range(m):
    print()
    x = int(input())
    A.append(x)
element(A)
print(A)
