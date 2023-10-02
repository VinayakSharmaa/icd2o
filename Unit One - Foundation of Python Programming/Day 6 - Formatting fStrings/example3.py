import math


average = 67.4465446

print(f"{average}")
print(f"{average:.2f}")
print(f"{average:>20}")
print(f"{average:>20.2f}")
#print(f"{average.2f>20}) # does not work we need width/alignment first and decimal after

# print PI with 2 decimal places aligned right with a width of 10
print(math.pi)
print(f"{math.pi:>10.2f}")
