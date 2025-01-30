print("""
      Divisibilty Checker
""")

num= float(input("Enter a number: "))

if num %2 == 0  and num%3 ==0:
  print(f"The Number {num} is divisible by 2 & 3")
else:
  print(f"The Number {num} is NOT divisible by 2 & 3")
