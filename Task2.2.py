lst=[-1,2,5,-3,-4,-5,-6]
m=0
for i in lst:
    m+= abs(i)
print(m)


for  i in range(1, len(lst)):
    if lst[i]< m:
        m=lst[i]
print(m)

m=-float("inf")
print(m)
m>1111111



#3
n=int(input())
fact=1
for i in range(1, n+1):
    fact*=i
print(fact)