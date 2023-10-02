average = 12.65675765
print(f"{average}")
print(f"{average:.2f}") # This rounds the decimal to 2 places
print(f"{average:.3f}")

number = 6.2
print(f"{number:.2f}") # Adds a 0 to 6.1 making it 6.10

number = 6
print(f"{number:.2f}") # 6.00

math_mark = 34
math_total = 45

math_average = math_mark / math_total

print(f"{math_average}") # 0.755555555555
print(f"{math_average:.1%}") # 75.6%, rounded it to one decimal place and made it a percentage
print(f"{math_average:.1f}") # 0.8, rounded it to one decimal place.