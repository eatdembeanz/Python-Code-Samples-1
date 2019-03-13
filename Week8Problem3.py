#Benjamin Page
#3/7/2019

#Takes a list and checks if the value 5 is in that list.

checkedlist = []
listfinished = False
while listfinished != True:
    appendnum = int(input("Please enter a number to add to your list."))
    checkedlist.append(appendnum)
    checkfinish = str(input("Add another number to your list? Type no if finished."))
    if checkfinish == "no":
        listfinished = True
    else:
        listfinished = False
def Problem3(checkedlist):
    found5 = False
    i = 0
    while found5 == False:
        for i in checkedlist:
            if i == 5:
                found5 = True
            elif len(checkedlist) == 1:
                print("5 is NOT in the provided list.")
                return
            elif checkedlist[i] == len(checkedlist-1):
                print("5 IS NOT in the provided list.")
                return
            else:
                i = i+1
    if found5 == True:
        print("5 IS in the provided list.")
    
    return
Problem3(checkedlist)
