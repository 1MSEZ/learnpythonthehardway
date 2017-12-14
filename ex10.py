from sys import argv
#script shows the {script} name while launching the program
#user_name will be prompted for user to enter and will be displayed later on.
script, user_name = argv, input("Please enter your name:")
prompt = '>>> '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is, but I'm looking forward to search it up.
And you have a {computer} computer. Nice!
"""
)