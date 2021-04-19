import math

#SOLID_RECTANGLE 
def solidRect(width, height):
    for j in range(0, height):
        print("")
        for i in range(0, width):
            print("#",end="")
    print()




#BORDER_RECTANGLE
def bordRect(width, height):
    borderW = int(2)
    for j in range(0, height):
        print("")
        for i in range(0, width):
            if j < borderW or j > height - 1 - borderW or i < borderW or i > width - 1 - borderW:
                print("#", end="")
            else:
                print(" ", end="")
    print()

def checkPattern(width, height):
    for j in range(0, height):
        print("")
        for i in range(0, width):
            if (i+j) % 2 == 0:
                print("█", end="")
            else:
                print(" ", end="")
    print()

def pyramid(width, height):
    
    pyramidWidth = 2 * height - 1
    centerColum = height -1

    for j in range(0, height):
        print("")
        for i in range(0, pyramidWidth):
            if i >= centerColum - j and i <= centerColum + j:
                print("#", end="")
            else:
                print(".", end="")
    print()

def Circle(width, height):
    centerX = float(width/2.0)
    centerY = float(height/2.0)
    radius = 0.0

    if (height < width):
        radius = 0.5 * height
    else:
        radius = 0.5 * width
    
    for j in range(0, height):
        print("")
        
        for i in range(0, width):

            dx = i - centerX
            dy = j - centerY
            d = math.sqrt(dx * dx + dy * dy)

            if d < radius:
                print("#", end="")
            else:
                print(".", end="")
    print()





#Greetings
print("Let's create some cool ASCII art!")

#Input rectangle dim
print("Type a rectangle width: ")
widthString = input("Enter Rectangle width: ")
print(widthString)

print("Type a rectangle height: ")
heightString = input("Enter Rectangle height: ")
print(heightString)

#Convert strings to integers

width = int(widthString)
height = int(heightString)

print(width, type(width))
print(height, type(height))



print("SOLID RECTANGLE")
solidRect(width, height)

print("BORDER RECTANGLE")
bordRect(width, height)

print("CHECKER PATTERN")
checkPattern(width, height)

print("PYRAMID")
pyramid(width, height)


print("CIRCLE")
Circle(width, height)





