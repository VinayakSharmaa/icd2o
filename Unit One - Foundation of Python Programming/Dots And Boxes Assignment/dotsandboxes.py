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
print(f"{opponent1:>8} {yourpoints1:>22} {theirpoints1:>17} {percentage1:>104.2%}") 
print(f"{opponent2:>8} {yourpoints2:>22} {theirpoints2:>17} {percentage2:>104.2%}") 
print(f"{opponent3:>8} {yourpoints3:>22} {theirpoints3:>17} {percentage3:>104.2%}") 
print(f"{opponent4:>8} {yourpoints4:>22} {theirpoints4:>17} {percentage4:>104.2%}") 
print(f"{opponent5:>8} {yourpoints5:>22} {theirpoints5:>17} {percentage5:>104.2%}") 