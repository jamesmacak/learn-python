numbers = []

def add_nums_to_list(upper_bound, incrementor):
	i = 0
	while i < upper_bound:
		print(f"At the top i is {i}")
		numbers.append(i)

		i += incrementor
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")

def print_nums_from_list():
	print("The numbers: ")

	for num in numbers:
		print(num)

upper_bound = input("Enter the upper bound: ")
incrementor = input("Enter the incrementor: ")
add_nums_to_list(int(upper_bound), int(incrementor))
print_nums_from_list()

# using for-loops and range

print("Rewritten to use for-loops and range.")

numbers = []

def add_nums_to_list_again(upper_bound, incrementor):
	i = 0
	for i in range(0, upper_bound, incrementor):
		print(f"At the top i is {i}")
		numbers.append(i)

		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")

def print_nums_from_list_again():
	print("The numbers: ")

	for num in numbers:
		print(num)

add_nums_to_list_again(int(upper_bound), int(incrementor))
print_nums_from_list_again()