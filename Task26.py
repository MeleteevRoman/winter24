#Задание26-2
def dis(self):
    print(self.__dict__)

Pet=type('Pet',(),{'dis':dis})
my_pet=Pet()
my_pet.name="Tomas"
my_pet.age=7
my_pet.color='yellow'
my_pet.weight=23

my_pet.dis()