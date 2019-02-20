#Ben Page
#2/20/2019
#Iterates all integers from 1 to 50. Replaces numbers divisible by 5,3, or both 5 and 3 with a statement indicating that it's divisible.
for i in range(1,50):
    if i % 15 == 0:
        print("Divisible by both")
        continue
    elif i % 5 == 0:
        print("Divisible by five")
        continue
    elif i % 3 == 0:
        print("Divisible by three")
        continue
    else:
        print(i)
    
