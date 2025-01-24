import math
# Cosine , Sine , tan , Log , Factorial(!), Squareroot, ... {Sorry , we havent incorporated that scientific operation into  our system yet 😥🙂}
from Maths_operation import oper , result
from conditions import Emaths_accepted, sign

while Emaths_accepted:
  print("Please Enter a Valid Mathematical Operator😐")
  sign = input("Re-Enter an operational symbol use (/, + , x , -): ")

num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))
 
print(oper(sign, num1, num2))
questionaire1 = input("Do you want to perform any Scientific Operation? (Y or N): ")

if questionaire1.lower() == "y" or questionaire1.lower() == "yes":
  sci_operation = input("Enter your Scientific operation of choice (eg Sin, Cosine , tan , Factorial..): ")
  if sci_operation.lower() == "Cosine" or sci_operation.lower() == "cos":
    print(f"we want to access {result}")
  else:
    print("Good Byee 😥") 