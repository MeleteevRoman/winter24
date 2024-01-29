# Задание 6-1
R = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
     'M': 1000, 'IV' : 4, 'IX' : 9, 'XC' : 90, 'XL' : 40, 'CD' : 400, 'CM' : 900}
s = input()
s=s.upper()
prev = s[-1]
res = R[prev]
for cur in s[-2::-1]:
    if R[cur] >= R[prev]:
        res += R[cur]
    else:
        res -= R[cur]
    prev = cur
print(res)

# Задание 6-2
print(len(set(input().split(', ')) & set(input().split(', '))))

# Задание 6-3
s=(input().split())
res=set()
a=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
b=('1' '2' '3' '4' '5' '6' '7' '8' '9' '0')
b=str(b)
d=('!','@','$','#','%','^','&',"*",'(',')','-','_','+','+',':',';',',','<','>','.',"/",'"','[',']','|','{','}')
v,c,x='','',''
for w in s:
    res=res.union(set(list(w)))
    for i in res:
        if i in a:
            v += i+' '
        if i in b:
            c += i+' '
        if i in d:
            x += i+' '
print(v)
print(c)
print(x)
