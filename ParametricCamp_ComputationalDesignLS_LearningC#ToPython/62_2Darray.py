
#Parameters of our building

floors = int(7)
aptsPerFloor = int(5)

#2D array defining apartment names and wether if they have mail or not

apartments = str([floors, aptsPerFloor])
hasMail = bool([floors, aptsPerFloor])


#Initialize values with a nested for loop
arr = []

for i in range(0, floors):
    for j in range(0, aptsPerFloor):
        apartments = [i,j]
        hasMail = False

        arr.append(apartments)



#Some algorithm that tracks mail and updates 'hasMail'...
for x in arr:
    hasMail = False
    

    #Check mail in all apartments
    if x == [3,2]:
        hasMail = True
    elif x == [6,0]:
        hasMail = True
    
    print(x, hasMail)

















        



