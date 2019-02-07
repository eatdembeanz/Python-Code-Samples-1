# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).


#Benjamin Page
#2/7/2019
#Found issue with unclosed parentheses, not representing the input as an integer, and improper use of inverted commas (') causing a string to end early.
#Also found problem with improper operand (&& instead of &) and elif statement that should be else statement.
year = int(input("Greetings! What is your year of origin?"))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 & year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")
