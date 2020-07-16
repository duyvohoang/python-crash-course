# Exercise 3.8 of the "Python Crash Course" book
places = ['new york', 'hawaii', 'tokyo', 'paris', 'london']

print(places)
print("\n")

print(sorted(places))
print("This is the original list:")
print(places)
print("\n")

print(sorted(places, reverse=True))
print("This is the original list:")
print(places)
print("\n")

places.reverse()
print(places)
print("\n")

places.reverse()
print(places)
print("\n")

places.sort()
print(places)
print("\n")

places.sort(reverse=True)
print(places)
print("\n")