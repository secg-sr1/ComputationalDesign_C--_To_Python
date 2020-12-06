#Class Methods
#Class Example 05
import datetime



x = datetime.datetime.now()
print(x)

currentYear = int(x.strftime("%Y"))


class Person:
    #Fields
    name: str
    YOB: int
    height: float
    isAlive: bool
    
    #Constructor
    def __init__(self, name, YOB, height):
        self.name = name
        self.YOB = YOB
        self.height = height
        
        currentYear = int(x.strftime("%Y"))
    
        if self.YOB > currentYear:
            self.isAlive = True
        else:
            self.isAlive = False
    def __bool__(self):
        return self.isAlive
    
    def Greet(self):
        print("Hi! I am " + self.name)
    
    def Greet(self, otherName):
        print("Hi " + otherName + "! I am " + self.name)
    
    def Greet(self, otherName):
        print("Hi " + otherName.name + "! I am " + self.name)
    
    def Die(self):
        self.isAlive = False
    
    def GetAge(self):
        return int(currentYear) - int(self.YOB)


    
p = Person("Jose Luis", 1950, 5.9)
mj = Person("MaryJane", 2000, 4.2)

#p.Greet()
#mj.Greet()

p.Greet(mj)
#mj.Greet()

print(p.isAlive)
p.Die()
print(p.isAlive)
p.Die()
#p.Die()

age = p.GetAge()
print(age)
