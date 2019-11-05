Age = int(input('Enter your current age (In digits) > '))

BYear = 2019 - Age

if BYear % 4 != 0:
    print ("You were born in year %s" %(BYear))
    print ("Which is not a leap year!")

if BYear % 4 == 0:
    print ("You were born in year %s" %(BYear))
    print ("Which is a leap year!! WEEHEE!")
    
# print year in range(2020, 2036, 4):
#     Weight = Weight + HowMuch
#     print ("Your weight" %(year, Weight))




    

