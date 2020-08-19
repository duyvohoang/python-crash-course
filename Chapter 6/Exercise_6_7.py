# Exercise 6-7 of the book "Python Crash Course"

people = []

person = {
	'first_name': 'david',
	'last_name': 'smith',
	'age': 45,
	'city': 'new york',
	}
people.append(person)

person = {
	'first_name': 'vicent',
	'last_name': 'wilhem',
	'age': 30,
	'city': 'chicago',
	}
people.append(person)

person = {
	'first_name': 'john',
	'last_name': 'landrum',
	'age': 50,
	'city': 'san jose',
	}
people.append(person)

for person in people:
	full_name = person['first_name'] + " " + person['last_name']
	age = person['age']
	city = person['city']
	print(f"{full_name.title()} is {age} and living in {city.title()}.")