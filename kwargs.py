##kwargs - key word arguments
# Dictionary of key word arguments {key:value} name=Jerry
#

def greet (name, nationality):
    print ("Hello", name, "welcome to", nationality)

greet ("Jerry", "Brazil")    

def greet (name="Jerry", nationality="Brazil"):
    print ("Hello", name, "!", "welcome to", nationality)

greet () 


#kwargs Profile

def employee(**kwargs):
    print (kwargs)

employee (name="Jane", age=30, position="Developer")
employee (name="John", age=25, position="Designer", salary=50000)
employee (name="Jerry", age=35, position="Manager", department="Sales")

