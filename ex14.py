# this one is like the scripts with argv
#*args takes all the arguments to the function
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")
	
# *args is actually pointless, this is the solution
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")
	
# this just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")
	
# this one takes no arguments since none has been assigned
def print_none():
	print("I got nothin'.")
	
print_two("Oscar","Tian")
print_two_again("Oscar","Tian")
print_one("First!")
print_none()
	
