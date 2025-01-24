result = None


def oper(sign, num1, num2):
  global result
  if sign == "x":
    result = num1 * num2
    return result
  elif sign == "+":
    result = num1 + num2
    print(f"The answer is {result}")
  elif sign == "-":
    result = num1 - num2
    print(f"The answer is {result}")
  else:
   result = num1  / num2
   print(f"The answer is {result}")
