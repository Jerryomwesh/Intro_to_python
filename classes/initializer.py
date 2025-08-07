
#initializer: constructor

# class Student():
#     def __init__(self, name, age, grade):
#         self.name = sai
#         self.age = age
#         self.grade = grade

#     def get_grade(self):
#         return self.grade

# sai.__init__  


class Student():
    def __init__(self,name,age,grade):
        print("This is the first student")
        # print(name)
        # print(age)
        # print(grade)
        self.name = name
        self.age = age
        self.grade = grade

    def another_one(self,name,stream,form):
        print("This is the second student") 

        self.name = name
        self.stream = stream
        self.form = form

           

Jane=Student(name="Jane", age=20, grade=10) #object from a class
print ("Name:",Jane.name)
print ("Age:",Jane.age)
print ("Grade:",Jane.grade)








# sai=Student(name="Sai", age=20, grade=10) #object from a class
# print ("Name:",sai.name)
# print ("Age:",sai.age)
# print ("Grade:",sai.grade)
# sai.__init__()

# sai.another_one()

# Sai=Student(name="Sai", age=20, grade=10)
# print ("Name:",Sai.name)
# print ("Age:",Sai.age)
# print ("Grade:",Sai.grade)


# sai.another_one()

# jackson=Student.another_one(name="Jackson", stream="North", form="one")
# print ("Name:",jackson.name)
# print ("Stream:",jackson.stream)
# print ("Form:",jackson.form)