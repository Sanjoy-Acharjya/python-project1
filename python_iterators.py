mytuple = ("apple", "banana", "cherry")
myiter = iter(mytuple)
print(next(myiter))
print(next(myiter))
print(next(myiter))

mystr = ("banana")
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
          raise StopIteration
myobj = MyNumber()
myiter = iter(myobj)
  for x in myiter:
    print(x)




