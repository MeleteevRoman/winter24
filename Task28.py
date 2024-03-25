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

#Задание28-3
def TowerOfHanoi(n, x, y, z):
    if n == 1:
        print("Перемещаем диск 1 со стержня", x, "на стержень", y)
        return
    TowerOfHanoi(n - 1, x, z, y, )
    print("Перемещаем диск", n, "со стержня", x, "на стержень", y)
    TowerOfHanoi(n - 1, z, y, x)


n = 4

TowerOfHanoi(n, 'A', 'B', 'C')
print(2 ** n - 1)