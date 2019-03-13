#Benjamin Page
#3/7/2019

#Takes two inputs from a user and prints whether the sum is greater than, less than, or equal to 10.
num1 = int(input("Please enter Number 1"))
num2 = int(input("Please enter Number 2"))
def Problem2(num1,num2):
    sum = num1 + num2
    if sum > 10:
        print("Sum:",sum)
        print("Your sum is greater than 10.")
    elif sum < 10:
        print("Sum:",sum)
        print("Your sum is less than 10.")
    else:
        print("Sum:",sum)
        print("Your sum is equal to 10.")
    return

Problem2(1,10)
Problem2(1,2)
Problem2(1,9)
