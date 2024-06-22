y = 200
def myfunction1():
     print(y)
myfunction1()
print(y)

x = 100
def myfunction2():
    x = 150
    print(x)
myfunction2()
print(x)

def myfunction3():
    global x
    x = 400
    print(x)
myfunction3()
print(x)

def myfunction4():
  x = "Jane"
  def myfunction5():
    nonlocal x
    x = "Hello"
  myfunction5()
  return x
print(myfunction4())


