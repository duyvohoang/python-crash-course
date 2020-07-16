# Exercise 4.11 for the "Python Crash Course" book:

# Old code from the exercise 4-1:
pizzas = ['pepperoni', 'cheese', 'meat']

# New code:
friend_pizzas = pizzas[:]
friend_pizzas.append('vegetable')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza.title())

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza.title())