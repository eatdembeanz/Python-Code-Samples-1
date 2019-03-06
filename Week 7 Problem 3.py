#Benjamin Page
#2/28/2019
#Problem 3: Write a Python function to multiply all the numbers in a list. Use list [5, 2, 7, -1].

def listmult(numbers):
    import math
    product = 1
    for x in numbers:
        product *= x
    return product
print(listmult([5,2,7,-1]))
