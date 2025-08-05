# def extended_greetings (func):
#     def wrapper (name):
#         print ("Hello, welcome to the extended greetings!")
#         func(name)
#         print ("Hope you have a great day!")
#     return wrapper

# @extended_greetings
# def say_hi(name):
#     print (f"Hi {name}, how are you?")

# say_hi ("Alice")





def extended_greetings (func):
    def wrapper (*args, **kwargs):
        print ("Hello, welcome to the extended greetings!")
        func(*args, **kwargs)
        print (kwargs["height"])
        print ("Hope you have a great day!")
    return wrapper

@extended_greetings
def say_hi(name,age, height):
    print (f"Hi, my name is {name}, i am {age} years old and {height} tall")

say_hi (name= "Billie", age=30, height="5'9")