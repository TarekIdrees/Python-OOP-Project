class Animal(object):
    sleepHoursTable={'Rabbit':"6 to 8 Hours",'Cat':'15 Hours',
               'Horse':'2.5 Hours','Dog':'12 to 14 Hours',
               'Cow':'12 to 14 Hours','Duck':'10 Hours'}
    soundTable={'Rabbit':"Squeak",'Cat':'mewo',
               'Horse':'Neigh','Dog':'Howl',
               'Cow':'Moo','Duck':'Quack'}
    foodTable={'Rabbit':"vegetables not meat",'Cat':'meat and fish not fruit',
               'Horse':'Grass , haylage , fruit and vegetables not meat','Dog':'Salmon and chicken not Grapes or haylage',
               'Cow':'Grass not Grain','Duck':'Grapes and rice not meat'}
    def __init__(self):
        self.age = 0
        self.name = None
        self.numberOfLegs = 0
        self.numberOfHands = 0
        self.numberOfWings = 0
        self.skinColor = None
        self.gender = None
        self.weight = 0
        self.voice = None
        self.sleepHours=0
    def shadow(self,other):
        if isinstance(other,Horse) or isinstance(other,Rabbit):
            print("True")
        else:
            print("False")
    def swim(self,other):
        if isinstance(other,Dog) or isinstance(other,Duck):
            print("True")
        else:
            print("False")
    def foodTablePrint(self):
        print(Animal.foodTable)
    def soundTablePrint(self):
        print(Animal.soundTable)
    def sleepTablePrint(self):
        print(Animal.sleepHoursTable)
class Rabbit(Animal):
    Tag=30
    def __init__(self,name,age,gender,skin,weight):
        self.age = age
        self.name = name
        self.numberOfLegs = 2
        self.numberOfHands = 2
        self.skinColor = skin
        self.gender = gender
        self.weight = weight
        self.voice = 'squeak'
        Rabbit.Tag+=1
        print("rabbit with id ",self.Tag,"Has Been Added")
class Cat(Animal):
    Tag = 0
    def __init__(self, name, age, gender, skin, weight):
        self.age = age
        self.name = name
        self.numberOfLegs = 2
        self.numberOfHands = 2
        self.skinColor = skin
        self.gender = gender
        self.weight = weight
        self.voice = 'squeak'
        Cat.Tag += 1
    def play(self,other):
        if isinstance(other,Dog):
            print("True")
        else:
            print("False")

class Horse(Animal):
    Tag = 0
    def __init__(self, name, age, gender, skin, weight):
        self.age = age
        self.name = name
        self.numberOfLegs = 4
        self.skinColor = skin
        self.gender = gender
        self.weight = weight
        self.voice = 'Meow'
        self.sleepHours = '15 Hours'
        Horse.Tag += 1

class Cow(Animal):
    Tag = 80
    def __init__(self, name, age, gender, skin, weight):
        self.age = age
        self.name = name
        self.numberOfLegs = 4
        self.skinColor = skin
        self.gender = gender
        self.weight = weight
        self.voice = 'Moo'
        self.sleepHours = '12 to 14 Hours'
        Cow.Tag += 1
        print(self.name," with id ",self.Tag,"Has Been Added")
class Duck(Animal):
    Tag = 0
    def __init__(self, name, age, gender, skin, weight):
        self.age = age
        self.name = name
        self.numberOfLegs = 2
        self.numberOfWings = 2
        self.skinColor = skin
        self.gender = gender
        self.weight = weight
        self.voice = 'Quack'
        self.sleepHours = '10Hours'
        Duck.Tag += 1
class Dog(Animal):
    Tag = 0
    def __init__(self, name, age, gender, skin, weight):
        self.age = age
        self.name = name
        self.numberOfLegs = 4
        self.skinColor = skin
        self.gender = gender
        self.weight = weight
        self.voice = 'Howl'
        self.sleepHours = '12 to 14 Hours'
        Dog.Tag += 1

for i in range (20):
    cn='Cow'+str(i+1)
    c=Cow(cn,5,"female",'White with black',500)
for i in range (20):
    rn='Rabbit'+str(i+1)
    r1=Rabbit(rn,12,"Male",'White',20)
c1=Cat("Lily",2,'female','Black',4)
d1=Duck("spark",1,"Male",'Black and white',1)
do=Dog("spoony",4,"Male",'Creamy',6)
h1=Horse("Lucky",5,'female','Brown',18)
c2=Cat("Kitty",3,"female","Creamy",4)
r2=Rabbit("Bunnie",2,"Male",'White',4)
A=Animal()
A.foodTablePrint()
A.sleepTablePrint()
A.soundTablePrint()
c1.play(r1)
A.shadow(h1)
A.swim(d1)