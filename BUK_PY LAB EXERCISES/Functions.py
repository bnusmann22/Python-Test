#Basic Functions declaration

a  = float(input("Enter First number: "))
b  = float(input("Enter second number: "))

def add_nums(a, b):
  return a + b

print(f"The Sum is : {add_nums(a,b)}")


#Keyword args Function

def greet(name="Fatima"):
  print(f"Hello, {name}")

greet()
greet("Jamil")

# Handling Multipliple args

def average(*args):
  return sum(args)/len(args)

print(average(1,23,4,6,7))