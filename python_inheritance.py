class Person:
  def __init__(self, fname,lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("welcome,",self.firstname,  self.lastname,"to the class of", self.graduationyear)
obj = Student("John", "Doe",2020)
obj.welcome()







