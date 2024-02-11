# Задание 12-1
x = list(map(int, input('Введите список чисел: ').split()))
max_num=max(x)
min_num=min(x)
#print(min_num)
print(x)
max_ind=[index for index, i in  enumerate(x) if i==max_num]
min_ind=[index for index, i in  enumerate(x) if i==min_num]
print(f' Минимальное число списка:{min_num}\n',
      f'Максимальное число списка:{max_num}')
print(f'Список индексов элементов равных\n '
      f'минимальному значению списка Х:{min_ind}')
print(f'Список индексов элементов равных\n '
      f'максимальному значению списка Х:{max_ind}')

# Задание 12-2
a=[x for x in range(1,11) for i in range(x) ]
print(a)


s=[1,2,3,4,5,6,7,8,9,10]
res=[]
for w in s:
    for i in range(w):
        res.append(w)
print(res)

#Задание12-3
s = "1-2,4-4,3-6"
lst=[i for r in (list(map(int, q.split('-')))for q in s.split(",")) for i in range(r[0], r[-1]+1)]
print(lst)