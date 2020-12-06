#Iteration Break Statements
threshold = 500
firstValue = 0
firstSquare = 0

for i in range(0,50,1):
    if (i * i >= threshold):
        firstValue = i
        firstSquare = i*i
        break

print('The first square number %s is %s'%(threshold,firstSquare))
