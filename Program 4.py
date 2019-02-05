#Benjamin Page
#January 31, 2019

#Asks the user to put in information about their holiday (starting day, length), then calculates the day they'll come back.
day = str(input("Please enter the weekday you begin your holiday: "))
if day == "sunday":
        day = int(0)
if day == "monday":
       day = int(1) 
if day == "tuesday":
        day = int(2)
if day == "wednesday":
        day = int(3)
if day == "thursday":
        day = int(4)
if day == "friday":
        day = int(5)
if day == "saturday":
        day = int(6)
else:
        print("Error. Please enter a valid weekday.")

stay = int(input("Please enter the number of days you will be staying on holiday: "))
trip = day + stay
trip = trip % 7
if trip == 0:
        trip = str("sunday")
if trip == 1:
        trip = str("monday")
if trip == 2:
        trip = str("tuesday")
if trip == 3:
        trip = str("wednesday")
if trip == 4:
        trip = str("thursday")
if trip == 5:
        trip = str("friday")
if trip == 6:
        trip = str("saturday")
print(trip)
