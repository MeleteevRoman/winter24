#Задание28-1
a=[5,4,3,2,1]
#a=[1,2,3,4,5]

def Inv(a, n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] > a[j]):
                count += 1
    return count

n = len(a)
print("Число инверсий: ",Inv(a, n))