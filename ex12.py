from sys import argv

script, filename = argv, input("Please enter the name of the file you want to open: ")

print(f"We're going to erase {filename}.")
print("If you don't want that, just hit CTRL-C.")
print("If you do want that, hit RETURN.")

input("Have you decided yet?")

print("good choice,")
print("opening the file...")
#'w' is open for writing truncating the file first
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we're going to close it.")
target.close()