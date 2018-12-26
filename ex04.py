# Make a variable named 'cars' that contains an integer value of '100'
cars = 100
# Make a variable named 'space_in_a_car' that contains a double value of '4.0'
space_in_a_car = 4.0
# Make a variable named 'drivers' that contains an integer value of '30'
drivers = 30
# Make a variable named 'passengers' that contains an integer value of '90'
passengers = 90
# Make a variable named 'cars_not_driven' that contains an integer value of the difference between 'cars' and 'drivers'
cars_not_driven = cars - drivers
# Make a variable named 'cars_driven' that contains an integer value corresponding to 'drivers'
cars_driven = drivers
# Make a variable named 'carpool_capacity' that contains the double value of 'cars_driven' times 'space_in_a_car'
carpool_capacity = cars_driven * space_in_a_car
# Make a variable named 'average_passengers_per_car' that contains the quotent of 'passengers' and 'cars_driven'
average_passengers_per_car = passengers / cars_driven

# The following print statements will display hard coded text, followed by a variable (as text), followed by more hard coded text.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
