from scientific_operation import sci_Func
# Cosine , Sine , tan , Log , Factorial(!), Squareroot, ... {Sorry , we havent incorporated that scientific operation into  our system yet 😥🙂}
from Maths_operation import oper
from conditions import Emaths_accepted, sign

while Emaths_accepted:
  print("Please Enter a Valid Mathematical Operator😐")
  sign = input("Re-Enter an operational symbol use (/, + , x , -): ")
  if sign == "x" or sign =="+" or sign =="/" or  sign =="-":
    break

num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))

if sign == "/" and num2 == 0:
  print(f"Division Cannot occur with {num2}")
 
print(f"The Result of {num1} {sign} {num2} is : {oper(sign, num1, num2)}")

new_result = oper(sign, num1, num2)
questionaire1 = input("Do you want to perform any Scientific Operation? (Y or N): ")

if questionaire1.lower() == "y" or questionaire1.lower() == "yes":
  sci_operation = input("Enter your Scientific operation of choice (eg Sin, Cosine , tan , Factorial..): ")
  print(sci_Func(sci_operation , new_result))
else:
  print("""
         Thank You For Trying our App 🤗💕

              Made with 💕 , by Dev Jamil🚀
           """) 