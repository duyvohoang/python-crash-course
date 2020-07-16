# Exercise 3.5 of the "Python Crash Course" book.

# The below code is from the 3.4 exercise:
guests = ['john dewey', 'albert einstein', 'elon musk']
print(f"Hi {guests[0].title()}, do you want to have dinner with me?")
print(f"Hi {guests[1].title()}, do you want to have dinner with me?")
print(f"Hi {guests[2].title()}, do you want to have dinner with me?")

# New code for the 3.5 exercise:
removed_guest = 'john dewey'
print(f"\nHi everyone, {removed_guest.title()} cannot join with us.")
guests.remove(removed_guest)
guests.append('vicent nguyen')
print(f"Hi {guests[0].title()}, do you want to have dinner with me?")
print(f"Hi {guests[1].title()}, do you want to have dinner with me?")
print(f"Hi {guests[2].title()}, do you want to have dinner with me?")