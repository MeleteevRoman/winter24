#Задание 23-1
s=input('Введите строку: ')
m = ""

for i in range(len(s)):
    for j in range(len(s), i, -1):
        if len(m) >= j-i:
            break
        elif s[i:j] == s[i:j][::-1]:
            m = s[i:j]
            for x in range (len(m)):
                x+=1

print(f'Длиной подстроки с наибольшим палиндромом является {x}(подстрока "{m}")')
#Задание23-2
import psycopg2
import pandas as pd
con=psycopg2.connect(
    database="postgres",
    user="postgres",
    password="hjvfhjvf",
    host="127.0.0.1",
    port="5432"
)
cur=con.cursor()
cur.execute('''SELECT * FROM book
ORDER BY book_id''')
rows=cur.fetchall()


d=[]
for  row in rows:
    d.append(row)
df = pd.DataFrame(d, columns=['book_id', 'title','author','price','amount','total','author_id'])
print(df)

con.close()
#Задание23-3
import itertools
lst = input('Введите список чисел: ').split()

res = int(max((''.join(i) for i in itertools.permutations(str(i)
                for i in lst)), key=int))
print('Самое большое число: ' + str(res))
