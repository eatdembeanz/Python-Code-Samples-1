#Benjamin Page
#3/7/2019

#Checks whether your game character has picked up all the items needed to perform a certain task, and checks against any status debuff.

playerinv = ["pan","paper","idea","rope","groceries"]
playerstat = ["slow"]
def Problem5(playerinv,playerstat):
    if "rope" in playerinv and "coat" in playerinv and "first_aid_kit" in playerinv:
        if "slow" in playerstat:
            Task1 = "Cannot climb a mountain while slow!"
        else:
            Task1 = "Prepared to climb a mountain!"
    else:
        Task1 = "Not equipped to climb a mountain!"
        
    if "pan" in playerinv and "groceries" in playerinv:
        if "small" in playerstat:
            Task2 = "Cannot cook a meal while small!"
        else:
            Task2 = "Prepared to cook a meal!"
            
    else:
        Task2 = "Not equipped to cook a meal!"
    if "pen" in playerinv and "paper" in playerinv and "idea" in playerinv:
        if "confusion" in playerstat:
            Task3 = "Cannot write a book while confused!"
        else:
            Task3 = "Prepared to write a book!"
    else:
        Task3 = "Not equipped to write a book!"
        
    return(Task1,Task2,Task3)
print(Problem5(playerinv,playerstat))
