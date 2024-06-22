thisdist={
    "brand" : "Ford",
    "model" : "mustang",
    "year" : "2000",
    "earBirdModel" : "2020",
    "electric" : "False",
    "outsidecolors" : ["red","blue","white"],
    "insidecolors" : ("biscuit","purple","black")
}
print(thisdist)
thisdist.update({"year" : 2024})
print(len(thisdist))
print(type(thisdist))

print(thisdist["year"])
print(thisdist["brand"])

thisdict = dict(name="Sanjoy", age=40, country="Bangladesh",electric="True")
print(thisdict)

thisdictt = {
    "branded" : "toyota",
    "modell" : "2014",
    "name" : "premeo"
}
x = thisdictt.keys()
print(x)
x = thisdictt.get("name")
print(x)
thisdictt["color"] = "white"
x = thisdictt.keys()
print(x)
thisdictt["modell"] = "2020"
x = thisdictt.values()
print(x)
if "modell" in thisdictt:
    print("yes,'modell' exists in the dictionary")
    if "model" in thisdict:
        print("Yes, 'model' is one of the keys in the thisdict dictionary")

    thisdict1 = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
thisdict1["color"]="red"
print(thisdict1)
thisdict1.pop("brand")
print(thisdict1)

thisdict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict2.popitem()
print(thisdict2)

thisdict3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict3["model"]
print(thisdict3)

thisdict4 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict4.clear()
print(thisdict4)

thisdict5 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict5:
    print(x)

thisdict6 = {
     "brand": "Ford",
    "model": "Mustang",
     "year": 1964
    }
for x in thisdict6:
  print(thisdict6[x])

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
  for x in thisdict.values():
      print(x)

thisdict7 = {
     "brand": "Ford",
     "model": "Mustang",
    "year": 1964
  }
mydict= thisdict7.copy()
print(mydict)

thisdict8 = {
     "brand": "pajero",
     "model": "Mustang",
    "year": 2020
  }
mydict1= dict(thisdict8)
print(mydict1)

myfamily= {
    "child1" : {
    "name" : "Emil",
    "year" : 2004
},
    "child2" : {
    "name" : "john",
    "year" : 2008
},
    "child3" : {
    "name" : "Steve",
    "year" : 2010
}
}
print(myfamily)






