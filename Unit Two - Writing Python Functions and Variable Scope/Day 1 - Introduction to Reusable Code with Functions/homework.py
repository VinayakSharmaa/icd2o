length = int(input("please enter length "))
width = int(input("please enter width "))

def area_of_rectangle(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        return print(length * width)
    else:
        return print("Invalid input. Please provide numeric values for length and width.")
    
area_of_rectangle(length, width)

