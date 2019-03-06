#Benjamin Page
#2/28/2019
#Problem 4: Write a Python function that takes a list of numbers and returns a new list with unique elements of the first list.  Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append function.

def uniquelist(numbers):
    unique = []
    for x in numbers:
        if x not in unique:
            unique.append(x)
    return unique

print(uniquelist([1,3,3,3,6,2,3,5]))
        
        
