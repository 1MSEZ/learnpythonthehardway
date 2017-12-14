types_of_people = 10
#f adds the various of types of people into the sentence of x
x = f"there are {types_of_people} types of people."

#making a long variable name into it's abbriviation
binary = "Binary"
do_not = "don't"
#af adding the various of binary and don't into the sentense of y
y = f"Those who know {binary} and those who {do_not}."

#(x,y) prints out the command we did earlier
print(x)
print(y)
#Adding the variable of (x,y) into another sentense
print(f"I said: {x}")
print(f"I also said: '{y}'")

#set hilarious = False
hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"
#the .format() command determains what to put into {} bracket
print(joke_evaluation.format(hilarious))

#making a sentense into a quick accessable variable
w = "This is the left side of "
e = "a string with a right side."
#combined the sentense inside of the two variables
#+ is a function, when executing print(w + e) it will be converted into (+ w e) or (add w e)
print(w + e) 