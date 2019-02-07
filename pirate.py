#Benjamin Page
#2/7/2019
#Found problems with unclosed parentheses, and an 'elif' statement that should have been an else statement, also without a colon.
greeting = input("Hello, possible pirate! What's the password?")
if greeting in ("Arrr!"):
	print("Go away, pirate.")
else:
        print("Greetings, hater of pirates!")
