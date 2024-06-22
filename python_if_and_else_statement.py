a = 200
b = 100
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

a = 50
b = 60
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

c = 400
d = 400
print("c is greater than d") if c > d else  print("c and d are equal") if c == d else print("d is greater than c")

a = 200
b = 100
c = 300
if a > b and c > a:
    print("Both conditions are true")

aa = 200
bb = 100
cc = 300
if aa > bb or aa > cc:
    print("atleast one of the conditions will be true")

a1 = 200
b1 = 300
if not a1 > b1:
    print("a1 is not greater than b1")

x = 41
if x > 10:
    print("Above ten")
    if x > 20:
         print("and above twenty")
    else:
         print("but not above twenty")













