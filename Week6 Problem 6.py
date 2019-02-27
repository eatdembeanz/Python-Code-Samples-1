#Benjamin Page
#2/21/2019
#Calculates the factorial of a given value. Prints both the calculated value as well as the same value run through the math module.
import math
facto = int(input("Please input number to factorialize:"))
x = 1
for i in range(1,facto+1):
    x = x*i
print("Program-calculated factorial:",x)
print("Module-calculated factorial:",math.factorial(facto))
