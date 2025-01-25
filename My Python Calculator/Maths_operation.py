
def oper(sign, num1, num2):
  if sign == "x":
    result = num1 * num2
    return result
  elif sign == "+":
    result = num1 + num2
    return result
  elif sign == "-":
    result = num1 - num2
    return result
  else:
   result = num1  / num2
   return result
