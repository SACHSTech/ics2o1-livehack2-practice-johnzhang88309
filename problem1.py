"""
--------------------------------------------------------
Name: Right angle triangle calculator
Purpose: Calculate if a triangle is a right triangle

Creator: Zhang. J 
Date: 12/02/2021
--------------------------------------------------------
"""

print ("***** Right angle triangle calculator*****")
#Write out variables
side_1 = int(input("Enter length of side 1: "))
side_2 = int(input("Enter length of side 2: "))
side_3 = int(input("Enter length of side 3: "))

#Write out formulas and print statements
if (side_1 ** 2 + side_2 ** 2 == side_3 ** 2) or (side_1 ** 2 + side_3 ** 2 == side_2 ** 2) or (side_2 ** 2 + side_3 ** 2 == side_1 ** 2):
  print("It is a right triangle. ")
else: 
  print("It is not a right triangle. ")
