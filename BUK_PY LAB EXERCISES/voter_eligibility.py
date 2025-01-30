LEGAL_AGE = 18

print("""
        Voter Eligibility
    Check Your Eligibility Status 🙂
""")

age = int(input("Enter Your age: "))

while age < 1 or age > 100:
  print("Invalid Age")
  age = int(input("Re-Enter Your age: "))

if age >= LEGAL_AGE:
  print(f"Congrats , You are {age} yrs old , and Eligible to vote 🚀")
else:
  print(f"""
            Sorry , You are too young to vote😐
        You have to wait {LEGAL_AGE - age} years more , to be eligible 
""")