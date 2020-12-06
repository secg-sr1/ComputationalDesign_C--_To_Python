#Funtion overloads

a = 5
b = 7
c = 12
nums = [2,4,6,8,10]


def additionA(a,b):
    sum = a + b
    return sum

def additionB(a,b,c):
    sum = a + b + c
    return sum

def additionC(values):
    sum = 0
    for i in range(0, len(values)):
        sum += values[i]
    return sum


sumAB = additionA(a,b)
sumABC = additionB(a,b,c)
sumArray = additionC(nums)

print(sumAB)
print(sumABC)
print(sumArray)
