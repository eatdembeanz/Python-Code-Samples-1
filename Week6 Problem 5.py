#Benjamin Page
#2/21/2019
#Converts a given input from radians to degrees. Prints the converted value, as well as the same value run through the math module.
import math

rads = float(input("Enter the amount of radians you want to convert:"))
degs = rads * (180/math.pi)
print("Program-calculated degrees:",degs)
print("Module-calculated degrees:",math.degrees(rads))
