#from Main_calc import new_result

def __factorial(new_result):
  if type(new_result) == float or new_result < 0:
    print(f"The Factorial of {new_result} , doesnt exist😐")
  else:
    def factorial(new_result):
      if new_result == 0:
        return 1
      else:
        return new_result * factorial(new_result - 1)
  
__factorial(-10)