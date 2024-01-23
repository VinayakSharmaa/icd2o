#create a list
list = [6,3,3,5,1,2,-9,-4,1,-7.29,-17]

#iterate and print the list
#print(list)
for element in list:    
    print(element)    #element is the next element in the list

list = [1,2,3,4,5]
total = 0
for el in list:
    total += el

print(total)

print(sum(list))

for el in list:
    if el % 2 == 0:
        print(el)


smallest = list[0] # assume the smallest is lower than 0
if el < smallest:
    smallest = el