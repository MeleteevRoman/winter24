# Задание 7-1
import math
numbers = list(map(int, input("Введите числа через пробел: ").split()))
print(numbers)
lcm = numbers[0]
for i in range(1, len(numbers)):
    lcm = lcm * numbers[i] // math.gcd(lcm, numbers[i])
print(lcm)

# Задание7-2
def code(c, k):
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + k) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + k) % 26 + ord('A'))
    else:
        return c

def code_2(s, k):
    return ''.join([code(c, k) for c in s])

n=int(input('Введите шаг шифрования: '))
string = input("Введите шифруемую строку: ")
print(code_2(string, n))
