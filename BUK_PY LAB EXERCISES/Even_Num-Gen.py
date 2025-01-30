print("""

      Even Number Generator
    """)

enter_Limit = int(input("Enter the number: "))
while enter_Limit < 0:
  print("Please Enter a positive number")
  enter_Limit = int(input("Re-Enter the number: "))

print(f"All the positive Even Numbers before {enter_Limit} are ...")
if enter_Limit == 0:
  print("None")
for i in range(1, enter_Limit):
  if i%2 == 0:
    print(i)