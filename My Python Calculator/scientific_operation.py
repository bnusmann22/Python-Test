import math

def sci_Func (sci_operation , new_result):
  if sci_operation.lower() == "Cosine" or sci_operation.lower() == "cos":
    return(f"The {sci_operation} of {new_result} is : {(math.cos(new_result))}")
  elif sci_operation.lower() == "sin" or sci_operation.lower() == "sine":
    return(f"The {sci_operation} of {new_result} is : {round(math.sin(math.radians(new_result)))}")
  elif sci_operation.lower() == "tan" or sci_operation.lower() == "tangent":
    return(f"The {sci_operation} of {new_result} is : {math.tan(new_result)}")
  elif sci_operation.lower() == "fac" or sci_operation.lower() == "factorial" or sci_operation.lower() == "!":
    if type(new_result) == float or new_result < 0:
      return(f"The Factorial of {new_result} , doesnt exist😐")
    else:
       sci_operation = "Factorial"
       return(f"The {sci_operation} of {new_result} is : {math.factorial(new_result)}")
  else:
    return(f"""
           
      Sorry !! The {sci_operation} operation hasnt been Incorporated in our system yet 😥 
           
                  Thank You For Trying our App 🤗💕

                      Made with 💕 , by Dev Jamil🚀
           """)