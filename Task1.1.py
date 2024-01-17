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
a=x+y
b=x-y
c=x*y
d=x/y
e=x//y
if a>=b and a>=c and a>=d and a>=e:
    print(f"Наибольшее число x+y: {a}")
if b>=a and b>=c and b>=d and b>=e:
    print(f"Наибольшее число x-y: {b}")
if d>=a and d>=b and d>=c and d>=e:
    print(f"Наибольшее число x/y: {d}")
if e>=a and e>=b and e>=c and e>=d:
    print(f"Наибольшее число x//y: {e}")
if c>=a and c>=b and c>=d and c>=e:
    print(f"Наибольшее число x*y: {c}")
print()

#Task 1.3 Ввести два числа x и y. Напечатать второе по величине из чисел x+y,x-y,x*y,x/y,x//y
print("Ввести два числа x и y. Напечатать второе по величине из чисел x+y,x-y,x*y,x/y,x//y")
print("Введите число x:")
x = float(input())
print("Введите число y:")
y = float(input())
a = x + y
b = x - y
c = x * y
d = x / y
e = x // y
if a > b and a >= c and a > d and a > e:

    if b > c and b > d and b > e:
        print(f"Второе наибольшее число x-y: {b}")
    if d > b and d > c and d >= e:
        print(f"Второе наибольшее число x/y: {d}")
    if e > b and e > c and e >= d:
        print(f"Второе наибольшее число x//y: {e}")
    if c > b and c > d and c > e:
        print(f"Второе наибольшее число x*y: {c}")

if b > a and b > c and b > d and b > e:

    if a > c and a > d and a > e:
        print(f"Второе наибольшее число x+y: {a}")
    if d > a and d >= c and d >= e:
        print(f"Второе наибольшее число x/y: {d}")
    if e > a and e >= c and e >= d:
        print(f"Второе наибольшее число x//y: {e}")
    if c > a and c >= d and c >= e:
        print(f"Второе наибольшее число x*y: {c}")

if d > a and d > b and d > c and d >= e:

    if a > b and a > c and a > e:
        print(f"Второе наибольшее число x+y: {a}")
    if b > a and b > c and b > e:
        print(f"Второе наибольшее число x-y: {b}")
    if e > a and e > b and e > c and e < d:
        print(f"Второе наибольшее число x//y: {e}")
    if c > a and c > b and c > e:
        print(f"Второе наибольшее число x*y: {c}")

if e > a and e > b and e > c and e >= d:

    if a > b and a > c:
        print(f"Второе наибольшее число x+y: {a}")
    if b > a and b > c:
        print(f"Второе наибольшее число x-y: {b}")
    if d > a and d > b and d > c and d > e:
        print(f"Второе наибольшее число x/y: {d}")
    if c > a and c > b:
        print(f"Второе наибольшее число x*y: {c}")

if c >= a and c > b and c > d and c > e:

    if a > b and a > d and a > e and a>c:
        print(f"Второе наибольшее число x+y: {a}")
    if b > a and b > d and b > e:
        print(f"Второе наибольшее число x-y: {b}")
    if d > b and d >= e and d>a:
        print(f"Второе наибольшее число x/y: {d}")
    if  e > b and e >= d and e>a:
        print(f"Второе наибольшее число x//y: {e}")

print((a, b, c, d, e)