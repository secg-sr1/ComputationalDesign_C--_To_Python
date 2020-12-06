#Class Example03 
import datetime

x = datetime.datetime.now()
print(x)

class Person:
    #Fields
    name: str
    YOB: int
    height: float
    isAlive: bool
    
    #Constructor
    def __init__(self,name):
        self.name = "Cutie"
        self.YOB = int(x.strftime("%Y"))
        self.height = 2.0
        self.isAlive = True

baby = Person("Cutie")
print(baby.name)
print(baby.YOB)
print(baby.height)
print(baby.isAlive)
