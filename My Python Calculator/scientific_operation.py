import math

def sci_Func (sci_operation , new_result):
  operations = {
    "Cosine" = math.cos,
    "cos" = math.cos, 
    "sin" = lambda x: round(math.sin(math.radians(x))),
    "sine" = lambda x: round(math.sin(math.radians(x))),
    "tan" = math.tan, 
    "tangent" = math.tan,
    "fac" = math.factorial,
    "factorial" = math.factorial,
    "!" = math.factorial,
  }

sci_operation = sci_operation.lower()
if sci_operation in operation:
  

# def sci_Func (sci_operation , new_result):
#   if sci_operation.lower() == "Cosine" or sci_operation.lower() == "cos":
#     return(f"The {sci_operation} of {new_result} is : {(math.cos(new_result))}")
#   elif sci_operation.lower() == "sin" or sci_operation.lower() == "sine":
#     return(f"The {sci_operation} of {new_result} is : {round(math.sin(math.radians(new_result)))}")
#   elif sci_operation.lower() == "tan" or sci_operation.lower() == "tangent":
#     return(f"The {sci_operation} of {new_result} is : {math.tan(new_result)}")
#   elif sci_operation.lower() == "fac" or sci_operation.lower() == "factorial" or sci_operation.lower() == "!":
#     if type(new_result) == float or new_result < 0:
#       return(f"The Factorial of {new_result} , doesnt exist😐")
#     else:
#        sci_operation = "Factorial"
#        return(f"The {sci_operation} of {new_result} is : {math.factorial(new_result)}")
#   else:
    