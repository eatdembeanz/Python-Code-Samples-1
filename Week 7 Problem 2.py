#Benjamin Page
#2/28/2019
#Problem 2: Write a Python function to check whether a number is in a given range. Use range(1,10). Print whether the number is in or not in the range.

def rangecheck(y):
    if y in range(1,10):
        print("Number is within range.")
    else:
        print("Number is outside of range.")
