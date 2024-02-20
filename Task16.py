#Задание 16-1.
import re
def func(str):
    words = re.findall(r'\b([A-Za-z|А-Яа-я]{1}\w*)',text)
    i = ''.join([w[0].upper() for w in words])
    return i

text = input("Введите строку из слов: ")
print(func(text))

#Задание 16-2.

#Задание 16-3.
def lowercase_deco(func):
    def wrapper():
        origin_result=func()
        modi_result=origin_result.lower()
        return modi_result
    return wrapper
@lowercase_deco
def h():
    return 'HELLO WORLD, ПРИВЕТ МИР!'
print(h())