# basic import
from sys import argv

# takes two args, saves them appropiately
script, input_file = argv

# outputs the file using the .read() function
def print_all(f):
	print(f.read())

# set the file's object position to byte 0 (beginning)
def rewind(f):
	f.seek(0)

# print an individual line based on the line number (line_count) and file (f)
def print_a_line(line_count, f):
	print(line_count, f.readline())

# set working file to the input file from the cmd line
current_file = open(input_file)

# basic function calls
print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

# printing individual lines by means of incrementing the line counter
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file) # line 1

current_line = current_line + 1
print_a_line(current_line, current_file) # line 2

current_line = current_line + 1
print_a_line(current_line, current_file) # line 3

# more practice
print("\nMore practice\n")
rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line += 1 # increment total by 1
print_a_line(current_line, current_file) 

current_line += 1
print_a_line(current_line, current_file)