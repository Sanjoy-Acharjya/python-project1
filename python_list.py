thislist=["apple","banana","cherry"]
thislist[1:2]=["blackcurrant","watermelon"]
print(thislist)

thislist1=["apple","banana","cherry"]
thislist1[1:3]=["watermelon"]
print(thislist1)

thislist=["apple","banana","cherry"]
thislist.insert(2,"mango")
print(thislist)

thislist=["apple","banana","cherry"]
thislist.append("orange")
print(thislist)

thislist=["apple","banana","cherry"]
tropical=["mango","orange","pineapple"]
thislist.extend(tropical)
print(thislist)

thislist=["apple","banana","cherry"]
thistuple=("orange","papaya","malta")
thislist.extend(thistuple)
print(thislist)

thislist=["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)

thislist=["apple","banana","cherry","apple"]
thislist.remove("apple")
print(thislist)

thislist=["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

thislist=["apple","banana","cherry"]
thislist.pop()
print(thislist)

thislist=["mango","banana","cherry"]
del thislist[1]
print(thislist)

thislist=["mango","banana","cherry"]
thislist.clear()
print(thislist)

thislist=["mango","banana","cherry"]
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[1])

thislist = ["watermelon", "banana", "cherry"]
i=0
while i < len(thislist):
    print(thislist[i])
    i=i+1



