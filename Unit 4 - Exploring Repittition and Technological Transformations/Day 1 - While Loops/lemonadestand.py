import random
def weather_Customer():
    x = random.randint(1,4)
    if x == 1:
        y = random.randint(0,10)
        return y , "Rainy"
   
    elif x ==2:
        y = random.randint(5,20)
        return y , "Cloudy"
   
    elif x == 3:
        y = random.randint(10,30)
        return y , "Sunny"
    elif x == 4:
        y = random.randint(15,40)
        return y , "Hot + Sunny"
   
 
 
def price(weather, price):
    if weather == "Rainy":
        if price < 1:
            return "ok"
       
        else:
            return "No, too much money"
       
    if weather == "Cloudy":
        if price < 2:
            return "ok"
       
        else:
            return "No, too much money"
       
    if weather == "Sunny":
        if price < 3:
            return "ok"
       
        else:
            return "No, too much money"
       
    if weather == "Hot + Sunny":
        if price < 4:
            return "ok"
       
        else:
            return "No, too much money"
 
 
 
def noMoney(sign, lemonade, total):
    if sign * 0.15 + lemonade * 0.02 > total:
        return "You don't have enough money fool"
   
    else:
        return "ol"
 
 
   
 
   
 
flag = input("end to end. yes to start: ")
j = 1
print("Your original profit is 2$")
total = 2
profit = 0
 
print("It takes 0.02$ to make a glass of lemonade")
while flag != "end":
    print("Day" + str(j))
   
 
    customer, weather = weather_Customer()
    print("Today it is: " + weather)
 
    Valid = False
 
    while Valid == False:
   
        sign = int(input("Each sign costs 0.15$ to make. How many signs do you want to have? "))
        customer = customer + customer * sign / 10
        price = float(input("In cents. How much are you going to sell each lemonade? "))
        lemo = int(input("How much lemonade are you going to make? "))
 
        if noMoney(sign,lemo,total) == "You don't have enough money fool":
            print("You don't have enough money.")
 
        else:
            Valid = True
 
       
 
       
           
   
 
 
    if customer > lemo:
        profit = lemo*price - sign * 0.15 - lemo * 0.02
   
    elif lemo > customer:
        profit = round((customer * price) - sign * 0.15 - lemo * 0.02, 2)
 
    total = total + profit
 
   
 
    print("your profit is: " + str(profit))
    print("you now have: " + str(total))
    flag = input("end to end. yes to continue: ")
 
 
 
    j+=1