# # print("Hello, World")
# # print("Hello, World")

# # age = 10 
# # if (age >= 18):
# #   if(age > 20): 
# #     print("You can Drive and Own YOur Own Car")
# #   elif(age >= 25):
# #       print("You Should have a child now")
# #   else:
# #     print("you can only drive ")
# # else:
# #   print("You are too young Go home")


# # for i in range (10):
# #   print(i)

# # for i in range (1 , 100 , 15):
# #   print (i)

# # for char in "Fatima":
# #   print(char)

# #   age = 10
# #   while age <= 18 :
# #     print("You are too Young ..😎")
# #     age += 1
# #   print('You are now old Enough')

# # sum = 0;
# # for j in range (10):
# #   sum += j
# #   print(sum)

# # whitespace = '''
# #    hey , 
# #                  just checking up on you tho 
# #                                                       you good?

# # '''

# # tittle = "menu".upper()
# # print (tittle.center(20, "="))
# # print(whitespace)
# # print(len(whitespace))

# while True:
#     try:
#         age = int(input("Please enter your age: "))
#     except ValueError:
#         print("Sorry, I didn't understand that.")
#         continue

#     if age < 0:
#         print("Sorry, your response must not be negative.")
#         continue
#     if age == 0:
#         print("Sorry, you cannot be 0 years old.")
#         continue
#     else:
#         #age was successfully parsed, and we're happy with its value.
#         #we're ready to exit the loop.
#         break
# if age >= 18: 
#     print("You are able to vote in the Nigeria!")
# else:
#     print("You are not able to vote in the Nigeria.")



from turtle import *
speed(10)
color('blue')
bgcolor('green')
b = 200
while b > 0:
  right(b)
  forward(b * 3)
  b = b + 1