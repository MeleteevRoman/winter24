# Задача 8-1
code=""
def cod(code):
    code = input()
    if "АГ" or "ГА" in code:
        code=code.replace("АГ", "1").replace("ГА","2").replace("1","ГА").replace("2","АГ")
    if "ЦТ" or "ТЦ" in code:
        code = code.replace("ЦТ", "3").replace("ТЦ", "4").replace("3", "ЦАГТ").replace("4","ТАГЦ")
        print(code)

cod(code)


# Задача 8-2
lst= [list(map(int, input('Введите три списка из цифр: ').split())) for i in range(3)]
lsts=[]
def sort_m(x):
    return x
print(sorted( lst,key=len))
lsts=lst.sort( key=len)

def minus_abs(x):
    return -abs(x)
lsts=sorted(lst[0],key=minus_abs),sorted(lst[1],key=minus_abs),sorted(lst[2],key=minus_abs)
print(lsts)


# Задача 8-3

code = ['abab', 'xx', 'aaaaaaa', 'abcbab']

print(str(code))

res = sorted(code, key=lambda sub: len(list(set(sub))))
res.reverse()

print(str(res))