import re
txt = "The rain in Spain"
x = re.findall("\AThe", txt)
print(x)
if x:
  print("yes,there is a match!")
else:
  print("no match")

txt = "The rain in Spain"

 # Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
print(x)
if x:
  print("yes, there is at least one match")
else:
  print("No, ain word is not matched")

txt = "The rain in Spain"
# Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"ain\b", txt)
print(x)
if x:
  print("yes, the ain word is matched")
else:
  print("No match")

txt = "The rain in Spain"
# Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain",txt)
print(x)
if x:
  print("yes match.ain is present but not at the beginning of a word")
else:
  print("No match.ain is not present.")


txt = "The rain in Spain"
# Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"ain\B",txt)
print(x)
if x:
  print("yes match.ain is present but not at the beginning of a word")
else:
  print("No match.ain is not present.")









