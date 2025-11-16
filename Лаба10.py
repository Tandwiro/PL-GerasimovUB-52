# Практика 10
print('Практическая работа 10')
print('Номер 3.1')
file = open('Герасимов_УБ-52_ввод.txt', 'r')
lines = file.readlines()
file.close()

n1 = int(lines[0].strip())
a1 = []
for i in range(1, 1 + n1):
    row = list(map(int, lines[i].strip().split()))
    a1.append(row)

sym = True
for x in range(n1):
    for y in range(x + 1, n1):
        if a1[x][y] != a1[y][x]:
            sym = False
            break

file = open('Герасимов_УБ-52_вывод.txt', 'w')



for row in a1:
    file.write(' '.join(map(str, row)))

if sym:
    print('Матрица симметрична')
else:
    print('Матрица не симмнтрична')

file.close()
print()

print('Номер 3.2')
file = open('Герасимов_УБ-52_ввод.txt', 'r')
lines = file.readlines()
file.close()

n1 = int(lines[0].strip())
start = 1 + n1
size = lines[start].split()
n = int(size[0])
m = int(size[1])

a2 = []
for i in range(start + 1, start + 1 + n):
    numb = lines[i].split()
    a3 = []
    for num in numb:
        a3.append(float(num))
    a2.append(a3)

maxv = a2[0][0]
maxx, maxy = 0, 0
for x in range(n):
    for y in range(m):
        if a2[x][y] > maxv:
            maxv = a2[x][y]
            maxx = x
            maxy = y

if maxy != 0:
    for x in range(n):
        k = a2[x][0]
        a2[x][0] = a2[x][maxy]
        a2[x][maxy] = k

file = open('Герасимов_УБ-52_выв.txt', 'a')
for row in a2:
    for num in row:
        file.write(str(num) + " ")

file.close()
print("Готово")