# Test
# Task 1.1 Ввести два числа x и y. Напечатать сумму и произведение этих чисел(оператор + и *)
print("Ввести два числа x и y. Напечатать сумму и произведение этих чисел(оператор + и *)")
print("Введите число x:")
x=float(input())
print("Введите число y:")
y=float(input())
print(f"Сумма чисел= {x+y}")
print(f"Произведение чисел= {x*y}")
print()

# Task 1.2 Ввести два числа x и y. Напечатать наибольшее из чисел x+y,x-y,x*y,x/y,x//y
print("Ввести два числа x и y. Напечатать наибольшее из чисел x+y,x-y,x*y,x/y,x//y")
print("Введите число x:")
x=float(input())
print("Введите число y:")
y=float(input())
n1, n2, n3, n4, n5=x+y, x-y, x*y, x/y, x//y
m=n1
if n2>=m:m=n2
if n3>=m:m=n3
if n4>=m:m=n4
if n5>=m:m=n5
print(m)

#Task 1.3 Ввести два числа x и y. Напечатать второе по величине из чисел x+y,x-y,x*y,x/y,x//y

print("Ввести два числа x и y. Напечатать наибольшее из чисел x+y,x-y,x*y,x/y,x//y")
print("Введите число x:")
x=float(input())
print("Введите число y:")
y=float(input())
n1, n2, n3, n4, n5=x+y, x-y, x*y, x/y, x//y

if n1>= n2:
    m1=n1
    m2=n2
else:
    m1=n2
    m2=n2

if n3>=m1:
    m2=m1
    m1=n3
elif n3>=m2:
    m2=n3
if n4>=m1:
    m2=m1
    m1=n4
elif n4>=m2:
    m2=n4
if n5>=m1:
    m2=m1
    m1=n5
elif n5>=m2:
    m2=n5

print(m1, m2)ащк шт



