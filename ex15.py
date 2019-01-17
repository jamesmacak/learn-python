from sys import argv

# arguments of command
script, filename = argv

# open the file and save contents in 'txt'
txt = open(filename)

# reads from 'txt' then prints to console
print(f"Here's your file {filename}:")
print(txt.read())

# close the file BAD
# txt = close(filename)

# get user input for next file
print("Type the filename again:")
file_again = input("> ")

# open the file
txt_again = open(file_again)

# write file object to console
print(txt_again.read())

# close the file BAD
# txt_again = close(file_again)
