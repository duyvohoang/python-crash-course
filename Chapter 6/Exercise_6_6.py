# Exercise 6-6 of the book "Python Crash Course"

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

people = ['jen', 'david', 'phil', 'vincent']
for person in people:
	if person in favorite_languages.keys():
		print(f"Thank {person.title()} for taking the poll!")
	else:
		print(f"{person.title()}, you should take the poll.")