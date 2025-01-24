# i = int(input("Enter a num: "))

# while i < 10:
#   i += 1
#   if i == 5:
#     continue
#   print(i)
  

# Phone_num = "234-91-6015-2870"
 
# for c in Phone_num:
#   if c == "-":
#     continue
#   print(c)

# a = input("enter Names: ")
# b = input("enter Names: ")

# def mine(a , b = "Fatima" ): # b has a default keyword
#   print(f"Hello {a}")
#   print(f"Hi {b}")

# mine(a , b)

# num = int(input("Enter Nums seperated with comma(,): "))
# def addNums(*num):
#   sum = 0;
#   for n in num:
#     sum = sum + n;
#   print("Sum:", sum)

# addNums(num)

n = int(input("Enter a number to find the factorial: "))
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

