# Exercise 6-5 of the book "Python Crash Course"

rivers = {
	'nile': 'egypt',
	'amazon': 'brazil',
	'yangtze': 'china'
	}

for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}")

print("\n")
for river in rivers.keys():
	print(f"{river.title()}")

print("\n")
for country in rivers.values():
	print(f"{country.title()}")