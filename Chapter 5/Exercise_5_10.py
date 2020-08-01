# Exercise 5.10 of the book "Python Crash Course"

current_users = ['dave', 'phill', 'john', 'admin', 'joe']
new_users = ['DAVE', 'smith']
current_users_lower = [user.lower() for user in current_users]


for new_user in new_users:
	if new_user.lower() in current_users:
		print("You need to enter a new username.")
	else:
		print(f"\n{new_user} is available.")