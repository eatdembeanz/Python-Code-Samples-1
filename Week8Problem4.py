#Benjamin Page
#3/7/2019

#Determines whether a year is a leap year or not.

checkyear = int(input("Enter a specific year."))

def Problem4(checkyear):
    if checkyear % 400 == 0:
        is_leap = True
    elif checkyear % 100 == 0:
        is_leap = False
        return(is_leap)
    elif checkyear % 4 == 0:
        is_leap = True
    else:
        isleap = False
    return(is_leap)

print(Problem4(checkyear))
