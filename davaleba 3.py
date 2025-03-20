
#  #დავალება 1

# import math

# x = int(input("Enter number x : "))
# y = int(input("Enter number y : "))
# z = math.pow(x, y)
# print("x to the power of y is", z)




# # #დავალება 2

# import random

# random_number = round(random.uniform(1, 100), 1)
# print(random_number)





# # #დავალება 3

import datetime

year = int(input("Enter the year of birth: "))
month = int(input("Enter the month of birth: "))
day = int(input("Enter the day of birth: "))

birth_date = datetime.date(year, month, day)
day_of_week = birth_date.strftime("%A")
print("You were born on a", day_of_week)




# #დავალება 4

# import random

# suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
# values = ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2')
    
# random_suit = random.choice(suits)
# random_value = random.choice(values)
    
# print("The random card is", random_value, "of", random_suit)