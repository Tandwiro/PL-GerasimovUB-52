# 9.1
print("Номер 9.1")
def fac(x, n):
    if n == 0:
        return 1
    return (x / n) * fac(x, n - 1)

x = 8
n = 10
res = fac(x, n)
print(res)
print()

# 9.2
print("Номер 9.2")
def nat(a,b):
    if a == 0 and b == 0:
        return 1
    return a % b

a = 8
b = 10
res = nat(a,b)
print(res)
print()

# 9.3
print("Номер 9.3")
n = 12345
def obr(n):
    if n < 10:
        return 1
    return int(str(n % 10) + str(obr(n // 10)))

print(obr(n), n)