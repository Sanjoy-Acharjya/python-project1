thisset={"apple","banana","cherry","apple",True,False,0,1,2}
print(len(thisset))
print(thisset)

set1={"apple","banana","cerry","mango"}
set2={1,2,3,4}
set3={True,False,False}
set4={"apple","banana",True,False,12,56}
print(set1)
print(set2)
print(set3)
print(set4)
set5={"apple","banana",True,False,12,56}
print(type(set5))
thisset1=set(("apple","banana","cherry","apple",True,False,0,1,2))
print(thisset1)
thisset2=set(("mango","apple","banana","cherry","banana"))
print(thisset2)

thisset={"pappa","apple","banana","cherry"}
for x in thisset:
    print(x)

thisset = {"papa", "apple", "banana", "cherry"}
print("pappa" in thisset)

thisset = {"papaya", "apple", "banana", "cherry"}
thisset.add("strayberry")
print(thisset)

thisset1 = {"watermelon", "blackberry", "mango"}
thisset2 = {"malta","pineapple","mango"}
thisset1.update(thisset2)
print(thisset1)

thisset1 = {"watermelon", "blackberry", "mango"}
thislist=["malta","pineapple","mango","cucumber"]
thisset1.update(thislist)
print(thisset1)

thisset1 = {"watermelon", "blackberry", "mango"}
thisset1.remove("blackberry")
print(thisset1)

thisset1 = {"watermelon", "blackberry", "mango","apple","banana"}
thisset1.discard("watermelon")
print(thisset1)

thisset1 = {"watermelon", "blackberry", "mango"}
thisset1.pop()
print(thisset1)

thisset1 = {"watermelon", "blackberry", "mango"}
thisset1.clear()
print(thisset1)

thisset={"watermelon", "blackberry", "mango","apple","banana"}
for x in thisset:
    print(x)

set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)

set1={"ab","bb","bc"}
set2={1,2,3}
set3=set1|set2
print(set3)

set1={"a","b","c"}
set2={"John", "Elena"}
set3={1,2,3}
set4 = {"watermelon", "blackberry", "mango"}
myset=set1.union(set2 , set3 , set4 )
print(myset)

set1={"an","bn","cn"}
set2={"ab","bb","bc"}
set3={1,2,3}
set4 = {"watermelon", "blackberry", "mango"}
myset=set1 | set2 | set3 | set4
print(myset)

x={"a","b","c"}
y=(1,2,3)
z=x.union(y)
print(z)

x={"aa","bb","cc"}
y=[1,2,3]
z=x.union(y)
print(z)

set1={"abc","bbc","bcc"}
set2={1,2,3}
set3={"a","b","c"}
set1.update(set2,set3)
print(set1)

set1={"apple","banana","cherry"}
set2={"cherry","mango","lichi"}
set3={"cherry","mango","malta"}
set4=set1.intersection(set2,set3)
print(set4)

set1={"apple","mango","cherry"}
set2={"cherry","mango","lichi"}
set3={"cherry","mango","malta"}
set4=set1 & set2 & set3
print(set4)

set1={"apple","mango","cherry"}
set2={"cherry","mango","lichi"}
set3={"cherry","mango","malta"}
set1.intersection_update(set2,set3)
print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1)

set1={"apple","bananqa","mango"}
set2={"mango","watermelon","malta"}
set3=set1 & set2
print(set3)

set1={"apple","bananqa","mango"}
set2={"mango","watermelon","apple"}
set1.intersection_update(set2)
print(set1)


