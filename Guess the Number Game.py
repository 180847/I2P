import random

higher_value = 100
lower_value = 0
final_value = random.randint(lower_value,higher_value)
print (final_value)

input("Pick a number")
if input > final_value:
    print ("smaller")
elif input < final_value:
    print ("larger")

