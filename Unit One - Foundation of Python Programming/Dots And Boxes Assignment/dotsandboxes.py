name = input("Please enter your name: ")

print("GAME 1")
opponent1 = input("Please enter the name of your opponent: ")
yourpoints1 = int(input("Please enter the number of boxes you created: "))
theirpoints1 = int(input("Please enter the number of boxes your opponent created: "))

print("GAME 2")
opponent2 = input("Please enter the name of your opponent: ")
yourpoints2 = int(input("Please enter the number of boxes you created: "))
theirpoints2 = int(input("Please enter the number of boxes your opponent created: "))

print("GAME 3")
opponent3 = input("Please enter the name of your opponent: ")
yourpoints3 = int(input("Please enter the number of boxes you created: "))
theirpoints3 = int(input("Please enter the number of boxes your opponent created: "))

print("GAME 4")
opponent4 = input("Please enter the name of your opponent: ")
yourpoints4 = int(input("Please enter the number of boxes you created: "))
theirpoints4 = int(input("Please enter the number of boxes your opponent created: "))

print("GAME 5")
opponent5 = input("Please enter the name of your opponent: ")
yourpoints5 = int(input("Please enter the number of boxes you created: "))
theirpoints5 = int(input("Please enter the number of boxes your opponent created: "))

percentage1 = yourpoints1/36
percentage2 = yourpoints2/36
percentage3 = yourpoints3/36 
percentage4 = yourpoints4/36 
percentage5 = yourpoints5/36 





print("Dots and Boxes Score Tracker")

print(f"Player's Name: {name}")
print("Opponent            Your Points   Opponent Points      Box%")
print("===========================================================")
print(f"{opponent1:>8} {yourpoints1:>31} {theirpoints1:>49} {percentage1:>59.2%}") 
print(f"{opponent2:>8} {yourpoints2:>31} {theirpoints2:>49} {percentage2:>59.2%}") 
print(f"{opponent3:>8} {yourpoints3:>31} {theirpoints3:>49} {percentage3:>59.2%}") 
print(f"{opponent4:>8} {yourpoints4:>31} {theirpoints4:>49} {percentage4:>59.2%}") 
print(f"{opponent5:>8} {yourpoints5:>31} {theirpoints5:>49} {percentage5:>59.2%}") 