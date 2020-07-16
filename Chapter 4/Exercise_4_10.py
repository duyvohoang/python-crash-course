# Exercise 4-10 of the "Python Crash Course" book

# Old code from the 4-8 exercise:
cubes = [value**3 for value in range(1,11)]
for number in cubes:
	print(number)

# Code for the exercise 4-10:
print("\nThe first three items in the list are:")
for item in cubes[0:3]:
	print(item)

print("\nThree items from the middle of the list are:")
for item in cubes[3:6]:
	print(item)

print("\nThe last three items in the list are:")
for item in cubes[-3:]:
	print(item)