# Check if a number is positive.
number = 89
if number > 0:
    print(f"{number} is positive")

if number <= 0:
    print(f"{number} is not positive")

age = int(input("Please enter your age: "))
if age >= 18:
    print(f"You are {age} years old which means you can vote.")

if age < 18:
    print(f"You are {age} years old, so you are not old enough to vote.")

str = input("Please enter a String: ")

if len(str) == 0:
    print("The String is empty.")

if len(str) != 0:
    print("The string is not empty.")

def max_number(a, b): 
    if a > b:
        return a
    
    return b

print(max_number(4,5))
print(max_number(14,5))

def password_checker(password, user_input): 
    if password == user_input:
        return True
    
    return False

pwd = input("Password: ")
secret = "GJGHJSDJWD"
print(password_checker(pwd, secret))


def range_checker(num, lower, upper): 
    if lower <= num <= upper: 
        return True
    
    return False

a = int(input("Please enter a number between 1 and 10: "))

if range_checker(a, 1, 10) == True: 
    print("Good you listen to instructions!!!")

if range_checker(a, 1, 10) == False:
    print("Stinky")




