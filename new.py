#Question 1 

userFirstName = input("Enter Your FirstName: ")
lastName = input("Enter your  last Name: ")


while len(userFirstName) and len(lastName) == 0:
  print("Re-enter your names")
  userFirstName = input("Enter Your FirstName: ")
  lastName = input("Enter your  last Name: ")

age = int(input("Enter your age: "))

if age < 18: 
  print("How the hell did u enter Jamia😥😂")

print(f'Welcome {userFirstName + " " + lastName} , i heard You are {age} yrs old ')



## Question 2 

import math


radius = float(input("Enter radius: "))
Area = math.pi * radius**2
print(f"The area is {Area}")


# Question 3 

temp = float(input("Enter a temperature in celcius to be converted: "))
convert_to_celcius = (temp * (9/5) + 32)
print(convert_to_celcius)
