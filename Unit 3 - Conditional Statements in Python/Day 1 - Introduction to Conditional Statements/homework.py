#1
def caught_speeding(speed, is_birthday): 
    if is_birthday: 
        speed = speed - 5
    
    if speed <= 60: 
        return "No Ticket"
    
    if 61 <= speed <= 80: 
        return "Small Ticket"
    
    return "Big Ticket"


print(caught_speeding(73, True))
print(caught_speeding(83, True))
print(caught_speeding(83, False))

#2
def squirrel_play(temp, is_summer): 
    if is_summer: 
        if 60 <= temp <=100: 
            return True
        else: 
            return False
    else: 
        if 60 <=temp <= 90: 
            return True
        else: 
            return False