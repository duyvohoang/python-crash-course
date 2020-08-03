# Exercise 6-4 of the book "Python Crash Course"

glossary = {
	'indentations': 'refers to the spaces at the beginning of a code line',
	'comments': 'code lines that will not be executed',
	'multi line comments': 'insert comments on multiple lines',
	'creating variables': 'are containers for storing data values',
	'variable names': 'to name your variables',
	'assign values to multiple variables': 'to assign values to multiple variables',
	'output variables': 'use the print statement to output variables',
	'string concatenation': 'to combine strings',
	'global variables': 'are variables that belongs to the global scope',
	'built-in data types': 'Python has a set of built-in data types'
	}

for key, value in glossary.items():
	print(f"{key.title()}:\n\t{value}.")