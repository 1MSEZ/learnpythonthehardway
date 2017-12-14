#To execute this: python ex9.py value1 value2 value3
from sys import argv
print("please input 3 more variable values")
script, first, second, third = argv, input(),input(),input()

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)