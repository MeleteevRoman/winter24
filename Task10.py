#Задание 10-1

s=['Мой дядя самых честных правил \n',' Когда  не в шутку занемог\n']
with open ("test.txt",'w') as f:
    f.writelines(s)
with open ("test.txt") as f2:
    s=f2.readlines()
    print(s)

f_out=open("test1.txt",'w')
for line in reversed(list(open("test.txt"))):
    words = line.split()
    reversed_words = ' '.join(reversed(words))
    #print(reversed_words)
    f_out.write(reversed_words)
f_out.close()

f=open('test1.txt','r')
s=f.readline()
print(s)
f.close()