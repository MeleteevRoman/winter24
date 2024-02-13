# Задание 13-1.
def fun():
    i=1
    while True:
        if  i % 2==0:
            yield -i
            i+=1
        else:
            yield i
            i+=1

for i in fun():
   print(i, end=",")


#тЗадание 13-2.
lst=[]
def palindrom(lst):
    n = int(input('Введите число до которого надо '
                  'создать последовательность палиндромов: '))

    for i in range(1,n):
            num = str(i)
            if num == num[::-1]:
                yield num

for i in palindrom(lst):
   print(i, end=",")

# Задание 13-3.
lst=list(map(int, input('Введите список чисел: ').split()))
def fun1(lst):
    for i in lst:
        if  i % 2==0:
            continue
        else:
            yield i

for i in fun1(lst):
   print(i, end=",")