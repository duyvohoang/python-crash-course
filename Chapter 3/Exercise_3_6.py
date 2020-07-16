# Exercise 3.6 of the "Python Crash Course" book.

# The below code is from the 3.4 exercise:
guests = ['john dewey', 'albert einstein', 'elon musk']
print(f"Hi {guests[0].title()}, do you want to have dinner with me?")
print(f"Hi {guests[1].title()}, do you want to have dinner with me?")
print(f"Hi {guests[2].title()}, do you want to have dinner with me?")

# New code for the 3.6 exercise:
print("\nHi all, I just found a bigger table for us, let have some more people.")
guests.insert(0, 'thomas lee')
guests.insert(2, 'joana ponder')
guests.append('kyle shannon')
print(f"Hi {guests[0].title()}, do you want to have dinner with me?")
print(f"Hi {guests[1].title()}, do you want to have dinner with me?")
print(f"Hi {guests[2].title()}, do you want to have dinner with me?")
print(f"Hi {guests[3].title()}, do you want to have dinner with me?")
print(f"Hi {guests[4].title()}, do you want to have dinner with me?")
print(f"Hi {guests[5].title()}, do you want to have dinner with me?")