Price_Chocolate= float(16.90)
print("Price of Chocolate is"),(Price_Chocolate)
payed=input("Please Enter Amount of Coins")

print("you payed"),(payed)
if payed > Price_Chocolate:
    change= payed-Price_Chocolate
    print("Your Change is"),(payed-Price_Chocolate)
if payed < Price_Chocolate:
    print("That is not enough you asshole")
if change > 0:
    print("your change is:")
while change > 50:
    change = change - 50
    print("50+")
while change > 20:
    change = change - 20
    print("20+")
while change > 10:
    change = change - 10
    print("10+")
while change > 5.0:
    change = change - 5.0
    print("5+")
while change > 2.0:
    change = change - 2.0
    print("2+")
while change > 1.0:
    change = change - 1.0
    print("1+")
while change > 0.5:
    change = change - 0.5
    print("0.5+")
while change > 0.2:
    change = change - 0.2
    print("0.2+")
while change >= 0.1:
    change = change - 0.1
    print("0.1+")
while change >= 0.01:
    change = change - 0.01

