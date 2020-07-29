# Exercise 5.2 of the book "Python Crash Course"
car_0 = 'toyota'
print(car_0 == "toyota")
print(car_0 != "toyota")

car_1 = "BMW"
print("\n")
print(car_1.lower() == "toyota")
print(car_1.lower() != "toyota")

price = 20_000_000
print("\n")
print(price == 10_000_000)
print(price != 10_000_000)
print(price > 10_000_000)
print(price < 10_000_000)
print(price >= 10_000_000)
print(price <= 10_000_000)

print("\n")
print(price >= 10_000_000 and price <= 30_000_000)
print(price < 10_000_000 or price > 30_000_000)

cars = ['toyota', 'bmw', 'subaru']
car_2 = 'nissan'
print("\n")
print(car_2 is cars)
print(car_2 not in cars)