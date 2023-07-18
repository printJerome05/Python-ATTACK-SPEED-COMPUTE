import math


atkspd = float(input("Enter the base attack speed: "))
atk = float(input("Enter hte bonus attack speed %: "))
lvl = float(input("Enter the level: "))





atk1 = atk / 100

lvll = lvl -1

total1 = atk1 * lvll

m1 = 1 + total1


total2 = atkspd * m1

total3 = round(total2, 3)

print ("The character's current attack speed is" , total3)
