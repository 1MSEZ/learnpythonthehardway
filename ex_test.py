print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
#Error 1 end without asking for an input()
height = input()
#Error 2 ending without a )
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
#module import required
from sys import argv

script, filename = argv, input("Now we are opening a file, input the file name:")
#filename
txt = open(filename)

print("Here's your file {filename}:")
#print (tx.read()) != 
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
#txt_again_read !=
print(txt_again.read())

#Error where having another ' inside ' '
print("Let's practice everything.")
#Error, don't skip a line without closing it, just use \n instead.
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#Error there should be a close " "on every print command.
print("--------------")
print(poem)
print("--------------")

#Error, what is the number after 3 -?
five = 10 - 2 + 3 - 6
#print bracket not closed with a parenthese )
print(f"This should be five: {five}")

#always add a :(colon) after defining something and start coding!
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
#what is the symbol between jars "?" 100
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
#Error, crates were not included
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

#startpoint != start_point again?
startpoint = start_point / 10

print("We can also do that this way:")
formula = secret_formula(startpoint)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
#Error, cats != cates
cats = 30
dogs = 15


if people < cats:
#parenthese is required for print command.
    print ("Too many cats! The world is doomed!")
#Error, should use people > cats instead of <
if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

#missing : 
if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

	#missing :, " for print
if people <= dogs:
    print("People are less than or equal to dogs.")

#== to check equal.
if people == dogs:
    print("People are dogs.")
