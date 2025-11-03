# Практика 5

print("Номер 3")
# n3 = input("Введите строку: \n")
n3 = "->.<- , ->.<-, ->.<-"
zam = n3.replace('.', '')

res = len(n3) - len(zam)
print("Кол-во замен: ", res)
print()


print("Номер 7")
n7 = "привет пока пакет"
n = len(n7)
pol = n//2
first = n7[:pol]
second = n7[pol:]

first = first.replace("п", "*")
res = first + second
print(res)


print("Номер 8")
n8 = "Дана строка, заканчивающаяся точкой ."
n8 = n8.strip(".")
m = n8.split()
print(m)
print("Кол-во слов в строке: ", len(m))
