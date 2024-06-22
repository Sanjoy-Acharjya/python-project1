f = open("demofile2.txt", "a")
f.write("Now the file has more content")
f = open("demofile2.txt", "r")
print(f.read())
f.close()

f = open("demofile3.txt", "w")
f.write("I have deleted the file from demo file3")
f.close()
f = open("demofile3.txt", "r")
print(f.read())
import sys
print(sys.version)







