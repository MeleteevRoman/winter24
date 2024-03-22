#Задание 27-1
def dartboard(n):
    row, top = 0, []
    for i in range(n, 0, -2):
        row += int('{:0^{}}'.format('1'*i, n))
        top.append(row)

        bottom = top[::-1][1:] if n%2 else top[::-1]


    return top + bottom


print(*dartboard(int(input("Введите число: "))),sep="\n")

#Задание27-3

# a = [[1,2,3],[4,5,6],[7,8,9],[7,8,111]]
a=[1,2,[3,4,[5]]]
# a=['x','y',['z']]
# a=[1,2,3]
#a=[]

count=0
for i in a:
    if type(i)==list:
        count+=1

        for j in  i:
            count+=1

            if type(j)==list:
                count+=1
    else :count+=1

print(count)