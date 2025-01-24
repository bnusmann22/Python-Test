DEFAULT_PASS = "King Jamil😎"
MAX_TRIALS = 3 

password = input("Please Enter your set Password: ")
trial = 0

if password == DEFAULT_PASS:
  print("Access Granted 😄")
else:
  while password != DEFAULT_PASS:
    trial += 1
    if trial < 3:
      print("Incorect Password 😐")
      print(f"You have {MAX_TRIALS - trial} trials left")
      password = input("Re Enter your Password: ")
    else:
      print("Password Trials Exceeded 🙄🥱")
      break


