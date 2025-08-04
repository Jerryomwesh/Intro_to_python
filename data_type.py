#Data Types in Python
# Python has several built-in data types that are used to store different kinds of data.

#indentation: 4 spaces

x=10 #Integer
print(x, type(x))
y=10.5 #Float  
print (type(y))
z="Hello" #String
is_active=True #Boolean
none_value=None #NoneType is the absence of a value or a null value


#Advanced Data Types
#List, Tuple, Set, Dictionary

#List: A list is an ordered collection of items that can be of different data types.
list1=[1,2,3,4,5,6,7,8,9,10]
print (type(list1 [1]))

#Set: A set is an unordered collection of unique items.
my_set={1,2,3,4}
print (type(my_set))

#Tuple: A tuple is an ordered collection of items that cannot be changed (immutable).
my_tuple = (1,2,3,"Apple",True) #my_tuple [3] wiil return "Apple"

#Dictionary: A dictionary is an unordered collection of key-value pairs.
my_dict = {"name": "John", "age": 30, "city": "New York"} #my_dict["name"] will return "John"
my_obj = {"key": "value", "age":23} #Dictionaries 
                                    #acts as objects in Python


