# Exercise 5.6 of the book "Python Crash Course"

age = 25
if age < 2:
	stage = "a baby"
elif age >= 2 and age < 4:
	stage = "a toddler"
elif age >= 4 and age < 13:
	stage = "a kid"
elif age >= 13 and age < 20:
	stage = "a teenager"
elif age >=20 and age < 65:
	stage = "an adult"
else:
	stage = "an elder"
print(f"You are {stage}.")