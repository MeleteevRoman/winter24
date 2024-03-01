#Задача 19-1
import itertools
lst = [10, 50, 100, 200, 500, 1000, 2000,5000]
for i in range(len(lst),0,-1):
    for x in itertools.combinations(lst, i):
        print(f'Сумма купюр {x} равна {sum(x)}')
        #print(sum(x), end=' ')

#Задача 19-2
class Fibonacci:
    def __init__(self):
        self.f1=0
        self.f2=1
    def __iter__(self):
        return self
    def __next__(self):
        self.f1,self.f2=self.f2,self.f1+self.f2
        return self.f1

fibonacci=Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

#Задача19-3
class Person:
    def __init__(self,name,name1,name2):
        self.name = name[::-1]
        self.name1=name1[::-1]
        self.name2=name2[::-1]
    def __str__(self):
        return f'# {self.name2}{self.name1}{self.name}'
    #def __repr__(self):
        #return str(self.__dict__)

p=Person("Иванов",'Михаил','Федорович')
print(p)