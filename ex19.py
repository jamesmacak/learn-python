# making the actual function, with two parameters, then simple txt output
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

# hardcoded values in the function call
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# set variables, then pass through the function call
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# calculate value of numbers within the function call
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# calculate value of variable + number within the function call
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# study drill 3
def got_milk(cookie_count, milk_count):
	print(f"There are {cookie_count} cookies.")
	print(f"There are {milk_count} glasses of milk.")
	print("Very tasty!")

# call 1
print("Basic variables")
cookie_count = 10
milk_count = 10
got_milk(cookie_count, milk_count)

# call 2
print("Direct call")
got_milk(20, 20)

# call 3
print("Math within call")
got_milk(20 + 10, 20 + 20)

# call 4
print("Variable math")
got_milk(cookie_count + 30, milk_count + 100)

# call 5
got_milk(cookie_count = input("User input straight into function call: "), milk_count = input("Now for milk: "))

# call 6
print("More legible user input")
cookie_count = input("Enter cookie amount: ")
milk_count = input("Enter milk amount: ")
got_milk(cookie_count, milk_count)

# call 7
print("Input without variables")
got_milk(input("Enter cookies: "), input("Enter milk: "))

# call 8
print("Input with math")
cookie_count = int(input("Enter Cookie: ")) + 10
milk_count = int(input("Enter milk: ")) - 10
got_milk(cookie_count, milk_count)

# call 9
print("One input, one hardcoded")
cookie_count = 1
milk_count = input("enter milk only: ")
got_milk(cookie_count, milk_count)

# call 10
print("One hardcoded (with math), one direct input (with typecasting & math)")
cookie_count = 2 + 4
got_milk(cookie_count, int(input("Enter milk: ")) + 7)