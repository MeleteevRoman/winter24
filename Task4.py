# Задание 4-1. Напишите калькулятор (простой).
a1, b, a2 = input("Напишите пример через пробелы: '2 + 2' и т.д.Для завершения введите три нуля: '0 0 0'. \nВведите пример: ").split()
a1=float(a1)
a2=float(a2)
while a1!=0 and b!="0" and a2!=0:
    if b == "+" :
        print(f"Ответ:  {a1 + a2}")
        a1, b, a2 = input("Введите пример: ").split()
        a1 = float(a1)
        a2 = float(a2)
    elif b == "-" :
        print(f"Ответ:  {a1 - a2}")
        a1, b, a2 = input("Введите пример: ").split()
        a1 = float(a1)
        a2 = float(a2)
    elif b == "*" :
        print(f"Ответ:  {a1 * a2}")
        a1, b, a2 = input("Введите пример: ").split()
        a1 = float(a1)
        a2 = float(a2)
    elif b == "/" :
        print(f"Ответ:  {a1 / a2}")
        a1, b, a2 = input("Введите пример: ").split()
        a1 = float(a1)
        a2 = float(a2)


# Задание 4-2. Вводим натуральное число n.
# Напечатайте спираль из чисел 1,2,3,...n*n
n = int(input("Введите число: "))
a = [[0] * n for i in range(n)]
count = 0
for i in range(n):
    count += 1
    a[0][i] = count
j = 0
i = n-1
n -= 1
while len(a)**2 != count:
    for k in range(n):
        j += 1
        count += 1
        a[j][i] = count
    for k in range(n):
        i -= 1
        count += 1
        a[j][i] = count
    for k in range(n-1):
        j -= 1
        count += 1
        a[j][i] = count
    for k in range(n-1):
        i += 1
        count += 1
        a[j][i] = count
    n -= 2
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

# Задание 4-3. Введите 2 проедложения содержащие пробелы, знаки препинания.
# Определить, являются ли эти предложения анограммами.
s1=input("введите первое предложение: ")
s2=input("Введите второе предложение: ")
s1=s1.lower()
s2=s2.lower()



dct1={}
dct2={}
print(s1, s2)
delt=('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', ' ', '.', '-', '+', '=', '!', '?')


for w in s1:
    if w in delt:
        s1=s1.replace(w,'')
for w in s2:
    if w in delt:
        s2=s2.replace(w,'')

for w in s1:
    if w not in dct1:
        dct1[w]=0
    dct1[w] +=1
print(dct1)
for w in s2:
    if w not in dct2:
        dct2[w]=0
    dct2[w] +=1
print(dct2)
if dct1==dct2:
    print(True)
else:
    print(False)