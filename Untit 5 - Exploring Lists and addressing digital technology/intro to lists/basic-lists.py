# Var = ["Geeks", "for", "Geeks"]
# print(Var)

# Python program to demonstrate
# Creation of List
 
# Creating a List
List = []
print("Blank List: ")
print(List)
 
# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)
 
# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])

# Append adds something to your list that you didn't add initially

list = []
list.append("hello")
list.append("Steve")
list.append("Abraham")
list.append("chicken")

print(list)

list.append(7)
print(list)

# You can append or add any type in the list (NOT undefined variables)

# Insert inserts an element at a certain index in an arra
list.insert(2, "Dev")
print(list)

#Remove removes an element from an array
list.remove("chicken")
print(list)

# Pop removes an element AND returns it from an array

who_left = list.pop(1)
print(list)
print(who_left)
