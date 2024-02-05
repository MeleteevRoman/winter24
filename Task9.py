# Задача 9-1
st="GCTA"
print(st)
dct={'G':"C",
     "C":"G",
     "T":"A",
     "A":"T"}
rna = ''
def rnk():
    rna = ''
    for i in st:
        rna += dct[i]
    print(rna)

rnk()

# Задача 9-2
buk = ('а', 'о', 'е', 'ё', 'у', 'ю', 'я', 'э', 'и', 'ы')
x = [i for i, c in enumerate(input('Введите слово: ')) if c in buk]
y = ''

for n in range(int(input("Введите количество вводимых слов для савнения: "))):
    word = input()
    if [i for i, c in enumerate(word) if c in buk] == x:
        y += word + ' '

print("Похожими словами являются: " + y)
