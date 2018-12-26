types_of_people = 10
# Puts integer variable inside of string variable
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# Puts two string variables inside of another string variable
y = f"Those who know {binary} and those who {do_not}."

# Prints two string variables
print(x)
print(y)

# Prints (using the formatter option) a string variable within a string
print(f"I said: {x}")
print(f"I also said: '{y}'") # Using single quotes within double quotes for style

hilarious = False
# Reserves a spot for a variable within the string variable (to be filled later)
joke_evaluation = "Isn't that joke so funny?! {}"

# Uses .format to place 'hilarious' inside of the string 'joke_evaluation'
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# Concatenates two strings together
print(w + e)
