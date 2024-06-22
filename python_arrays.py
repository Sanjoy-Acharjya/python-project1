cars = ["Ford", "Volvo", "Bmw"]
print(cars)
x = cars[1]
print(x)
cars[0] = "Toyota"
print(cars)

cars = ["Ford", "Volvo", "BMW", "Toyota"]
x = len(cars)
print(x)

cars = ["Ford", "Volvo", "BMW"]
cars.append("Toyota")
print(cars)

cars = ["Ford", "Volvo", "BMW", "Toyota"]
cars.pop(1)
print(cars)

cars = ["Ford", "Volvo", "BMW", "Volvo"]
cars.remove("Volvo")
print(cars)

fruits = ["apple", "banana", "cherry", "mango"]
x = fruits.copy()
print(fruits)

fruits = ["apple", "banana", "apple", "mango"]
x = fruits.count("apple")
print(x)

fruits = ["apple", "banana", "cherry"]
cars = ('ford', 'toyota', 'bmw')
fruits.extend(cars)
print(fruits)
