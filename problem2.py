"""
--------------------------------------------------------
Name: Vacation calculator
Purpose: Calculating a vacation

Creator: Zhang. J 
Date: 12/02/2021
--------------------------------------------------------
"""

print("***** Vacation Calculator *****")

#write out variables
mark = int(input("Please enter your average in school: "))
earnings_before_summer = int(input("Please enter your earnings before the summer: "))

#write out formulas and print statements
if mark >= 80 and earnings_before_summer >= 500: 
  print("You can have a vacation in Europe! ")
elif mark>= 80 and earnings_before_summer < 500:
  print("You can have a vacation in California!")
else: 
  print("You can not have a vacation")