import json
x = ('{"name":"John",'
     ' "age":40,'
     ' "city":"New York"}')
y = json.loads(x)
print(x)
print(type(x))
print(type(y))
print(y["name"],"is from", y["city"], "and his age ia", y["age"])

a = {
    "name":"Sanjoy",
    "city":"Dhaka",
    "age":35,
}
b = json.dumps(a)
print(b)
print(type(b))
print(type(a))

c = {
    "name": "Saumya",
    "city": "Dhaka",
    "age": 28,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(c, indent=4, separators=(". ", " = ")))





