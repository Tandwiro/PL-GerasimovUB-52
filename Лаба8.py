# Практика 8
print("Номер 3.1")
n = 2
a = []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

k = True
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] != a[j][i]:
            k = False
            break

if k:
    print("Симм")
else:
    print("Не симм")

print()

print("Номер 3.2")
# Строки
n = 2 # int(input())
# Столбцы
m = 3 # int(input())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

maxi = 0
maxj = 0
maxv = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > maxv:
            maxv = a[i][j]
            maxi = i
            maxj = j

if maxi != 0:
    a[0] = a[maxi]
    a[maxi] = a[0]

if maxj != 0:
    for i in range(n):
        a[i][0] = a[i][maxj]
        a[i][maxj] = a[i][0]

for row in a:
    print(' '.join([str(x) for x in row]))

print()

print("Номер 7.1")
n = 3
c = n * (n + 1) // 2
arr = list(map(int, input().split()))
a = [[0] * n for _ in range(n)]
k = 0

for i in range(n):
    for j in range(i, n):
        a[i][j] = arr[k]
        a[j][i] = arr[k]
        k += 1

for row in a:
    print(' '.join(map(str, row)))

print()

print("Номер 7.2")
n = 3
a = []
for i in range(n):
    row = list(map(float, input().split()))
    a.append(row)

k = 0
for i in range(n):
    k += a[i][j]
print(k)

if k != 0:
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                a[i][j] //= k

for row in a:
    print(' '.join([str(x) for x in row]))