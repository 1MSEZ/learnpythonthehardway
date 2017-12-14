from sys import argv
#Shows the script name
#filename requires input to load/open the txt 
script, filename = argv, input("please enter your file name: ")
#after seeing the .txt extension it will open the filename entered.
txt = open(filename)
#prints/read out the texts inside of the filename we entered.
print(f"Here's your file: {filename}")
print(txt.read())

txt.close()
#type the filename again to get another output
print("Type the file name again:")
file_again = input(">>> ")
#open the file again
txt_again = open(file_again)
#prints/read out the texts inside of the file again.
print(txt_again.read())

txt_again.close()
