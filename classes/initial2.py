

class Student():
    def __init__(self,gender):
        self.gender=gender
       


    def another_one(self,age,dob):
        self.age = age
        self.dob = dob

Adam=Student(gender="male")
print("Gender:",Adam.gender)



# Adam.another_one(age=25,dob=2017)
# print("Age:", Adam.age)
# print("DOB:", Adam.dob)


Eve=Student(gender="female")
Eve.another_one(dob=2018, age=26)
print("Age:", Eve.age)
print("DOB:", Eve.dob)
