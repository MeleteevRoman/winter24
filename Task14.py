# Задание 14-1.
def sumd(n):
    if n>=0:
        print(f'Количество цифр:  {len(str(n))}')
    else:
        sumd(-n)
    return n

n = int(input('Введите целое число: '))
sumd(n)

# Задание 14-2.
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)
n = int(input('Введите натуральное число: '))
print(f'Сумма цифр равна: {sum_of_digits(n)}')

# Задание 14-3.
def tri_2(n):
    print('*'* n)
    n-=1
    if n>=1:
        tri_2(n)
        n+=1
    if n==0:
        return
    print('*'* n)

    return
tri_2(int(input("Введите размер треугольников: ")))