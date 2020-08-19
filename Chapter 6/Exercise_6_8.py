# Exercise 6-8 of the book "Python Crash Course"
pets = []

pet = {
	'kind': 'dog',
	'owner': 'don',
}
pets.append(pet)

pet = {
	'kind': 'cat',
	'owner': 'maly',
}
pets.append(pet)

pet = {
	'kind': 'fish',
	'owner': 'david',
}
pets.append(pet)

for pet in pets:
	print(f"{pet['owner'].title()} has a {pet['kind']}.")