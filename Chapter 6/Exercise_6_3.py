# Exercise 6-3 of the book "Python Crash Course"

glossary = {
	'indentations': 'refers to the spaces at the beginning of a code line',
	'comments': 'code lines that will not be executed',
	'multi line comments': 'insert comments on multiple lines',
	'creating variables': 'are containers for storing data values',
	'variable names': 'to name your variables',
}
word = 'indentations'
print(f"{word.title()}:\n\t{glossary['indentations']}")

word = 'comments'
print(f"{word.title()}:\n\t{glossary['comments']}")

word = 'multi line comments'
print(f"{word.title()}:\n\t{glossary['multi line comments']}")

word = 'creating variables'
print(f"{word.title()}:\n\t{glossary['creating variables']}")

word = 'variable names'
print(f"{word.title()}:\n\t{glossary['variable names']}")