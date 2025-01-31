import math

def sci_Func(sci_operation, new_result):
    operations = {
        "cosine": lambda x: math.cos(x),
        "cos": lambda x: math.cos(x),
        "sine": lambda x: round(math.sin(math.radians(x))),
        "sin": lambda x: round(math.sin(math.radians(x))),
        "tangent": lambda x: math.tan(x),
        "tan": lambda x: math.tan(x),
        "factorial": lambda x: math.factorial(x) if x >= 0 and isinstance(x, int) else "doesn't exist",
        "fac": lambda x: math.factorial(x) if x >= 0 and isinstance(x, int) else "doesn't exist",
        "!": lambda x: math.factorial(x) if x >= 0 and isinstance(x, int) else "doesn't exist"
    }

    sci_operation = sci_operation.lower()
    if sci_operation in operations:
        result = operations[sci_operation](new_result)
        if "factorial" in sci_operation or sci_operation == "!":
            sci_operation = "Factorial"
        return f"The {sci_operation} of {new_result} is : {result}"
    else:
        return f"""
           
      Sorry !! The {sci_operation} operation hasn't been incorporated in our system yet 😥 
           
                  Thank You For Trying our App 🤗💕

                      Made with 💕 , by Dev Jamil🚀
           """