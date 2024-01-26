# Задача 5-1.Треугольник паскаля.
n = int(input("Введите число: "))
for i in range(n):
    print(' ' * (n - i))
    print(' '.join(map(str, str(11 ** i))))

# Задача 5-2
n = int(input('Введите число: '))

for i in range(1, n // 2 + 1):
    if n % i == 0:
        print(i, ' ', sep='', end='')
print(n)