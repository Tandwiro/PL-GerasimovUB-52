# Задачи "Практика 2"
import math
# Задание 1
print("Задание 1")
x = 14.26
y = -1.22
z = 3.5*10**(-2)

a = ( 2 * math.cos(x - 2/3) )
b = ( 1/2 + (math.pow(math.sin(y),2)))
c = 1 + (z**2) / (3 - z**2/5)

s1 = ((a / b) * c)
print(f"s = {s1:.6f}")
print("--------------")


# Задание 2
print("Задание 2")

x = -4.5
y = 0.75*10**(-4)
z = -0.845*10**2

s2 = (math.sqrt(9 + (x-y)**2)**(1/3) / (x**2 + y**2 + 2)) - math.exp(abs(x-y)) * (math.tan(z))**3
print(f"s = {s2:.5f}")
print("--------------")


# Задание 3
print("Задание 3")
x = 3.74 * 10 ** -2
y = -0.875
z = -0.16 * 10 ** 2

a = 1 + (math.sin(x + y))**2
b = x - (2*y) / (1 + x**2 * y**2)
znam = 2 + math.fabs(b)
c = (math.cos(math.atan(1 / z)))**2

s3 = a / znam + c
print(f"s = {s3:.5f}")
print("--------------")


# Задание 4
print("Задание 4")
x = 0.4 * 10 ** 4
y = -0.875
z = -0.475 * 10 ** -3

a = (math.cos(x) - math.cos(y))
znam = math.fabs(a) ** (1+2*(math.sin(y))**2)
b = (1 + z + (z**2 / 2) + (z**3 / 3) + (z**4 / 4))

s4 = znam * b
print(f"s = {s4:.5f}")
print("--------------")


# Задание 5
print("Задание 5")

x = -15.246
y = 4.642 * 10 ** -2
z = 21

a = math.log(y ** (math.sqrt(-x)))
znam = math.fabs(a)*(x-y/2)
b = math.sin(math.atan(z))**2

s5 = znam * b
print(f"s = {s5:.3f}")
print("--------------")


# Задание 6
print("Задание 6")
x = 16.55*10**-3
y = -2.75
z = 0.15

p1 = math.sqrt(x) + x ** (y + 2)
part1 = 10 * p1
sqrt = math.sqrt(part1)

part2 = math.asin(z) ** 2
znam = math.fabs(x-y)
part = part2 - znam

s6 = sqrt * part
print(f"s = {s6:.4f}")
print("--------------")


# Задание 7
print("Задание 7")
x = 0.1722
y = 6.33
z = 3.25 * 10**-4

part1 = 5 * math.atan(x)
part2 = (1/4) * math.acos(x)
num = x + 3 * math.fabs(x-y) + x**2 # нумиратор
denom = math.fabs(x-y) * z + x**2 # деномиратор
frac = num / denom

s7 = part1 - part2 * frac
print(f"s = {s7:.3f}")
print("--------------")


# Задание 8
print("Задание 8")

x = -2.235*10**-2
y = 2.23
z = 15.221

znam = math.exp(math.fabs(x-y))
part1 = znam * (math.fabs(x-y))**(x+y)
part2 = math.atan(x) + math.atan(z)
part1_2 = part1 / part2
part3 = (x**6 + math.log(y)**2) ** (1/3)

s8 = part1_2 + part3
print(f"s = {s8:.4f}")
print("--------------")


# Задание 9
print("Задание 9")

x = 1.825*10**2
y = 18.225
z = -3.298*10**-2

part = x**(y/x) - (y / x)**(1/3)
part1 = math.fabs(part)

num = y - x
denom = 1 + (y - x)**2
frac = num / denom
part2 = frac * math.cos(y)

part3 = - (z / (y-x))

s9 = part1 + part2 + part3
print(f"s = {s9:.5f}")
print("--------------")


# Задание 10
print("Задание 10")

x = 3.981*10**-2
y = -1.625*10**3
z = 0.512

part1 = 2 ** (-x)
sqrt_y = (math.sqrt(math.fabs(y))**(1/4))
sqrt_e = (math.sqrt(math.exp( (x-1) / (math.sin(z) ))) ) ** (1/3)
part2 = math.sqrt(x + sqrt_y)

s10 = part1 * part2 * sqrt_e
print(f"s = {s10:.5f}")
print("--------------")