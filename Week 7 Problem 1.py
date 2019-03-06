#Benjamin Page
#2/28/2019
#Problem : Write a function areaOfCircle(r)which returns the area of a circle of radius r.Make sure you use the math module in your solution
##Note that the function only works with floats and integers. 
def areaofcircle(x):
    import math
    A = math.pi * (x * x)
    return A
print(areaofcircle(5.5))
