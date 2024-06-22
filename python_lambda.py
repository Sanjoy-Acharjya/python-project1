x = lambda a: a + 10
print(x(5))

x = lambda a, b, c: a * b * c
print(x(2, 3, 4))

def my_function(n):
    return lambda a : a * n
mydoubler = my_function(5)
print(mydoubler(11))

def my_function(n):
    return lambda a : a * n
my_doubler = my_function(2)
my_tripler = my_function(3)
print(my_doubler(11))
print(my_tripler(11))


