price1 = 100
price2 = 59000
tax = 0.25
txt1 = f"The price is {95:.2f} dollars"
txt2 = f"The price is {30*20} dollars"
txt3 = f"The price is {price1 + (price1*tax)} dollars"
print(txt1)
print(txt2)
print(txt3)
txt4 = f"it is very {'expensive' if price1>50 else 'cheap'}"
print(txt4)
fruit1 = "AppLes"
fruit2 = "BaNaNa"
txt5 = f"I love {fruit1.upper()}"
txt6 = f"I love {fruit2.lower()}"
print(txt5)
print(txt6)
def myconverter(x):
  return x * 0.3048
txt7 = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt7)
txt8 = f"The price is {price2:,} dollars"
print(txt8)

