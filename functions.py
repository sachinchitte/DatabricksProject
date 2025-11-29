#Python Functions
def my_function():
  print("Hello from a function")

my_function()
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the actual value that is sent to the function when it is called.
def my_function1(name): # name is a parameter
  print("Hello", name)

my_function1("Emil") # "Emil" is an argument

#Default Parameter
def my_function(country = "Norway"):
  print("I am from", country)
my_function() #I am from Norway
my_function("India") #I am from India

#Keyword Arguments kwargs
def my_function(animal, name):
  print("I have a", animal,"named:",name) #I have a dog named: simba
my_function(name="simba",animal="dog")

#positional arguments
my_function("simba","dog") #I have a simba named: dog

#Mixing Positional and Keyword Arguments
my_function("simba",name="dog") #I have a simba named: dog

#*args and **kwargs
# #*args and **kwargs allow functions to accept a unknown number of arguments.

#Arbitrary Arguments - *args
#The *args parameter allows a function to accept any number of positional arguments.
#Inside the function, args becomes a tuple containing all the passed arguments:
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
print(my_function(1, 2, 3)) #6

#In this below example, "Hello" is assigned to greeting, and the rest are collected in names.
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

#Arbitrary Keyword Arguments - **kwargs
# keyword arguments will be passed into your function, add two asterisks ** before the parameter name
#The **kwargs parameter allows a function to accept any number of keyword arguments.
#Inside the function, kwargs becomes a dictionary containing all the keyword arguments
def my_function(**myvar):
  print("All data:", myvar) #All data: {'name': 'Tobias', 'age': 30, 'city': 'Bergen'}

my_function(name = "Tobias", age = 30, city = "Bergen")

#IMP
def my_function(title, *args, **kwargs):
  print("Title:", title) #Title: User Info
  print("Positional arguments:", args) #Positional arguments: ('Emil', 'Tobias')
  print("Keyword arguments:", kwargs) #Keyword arguments: {'age': 25, 'city': 'Oslo'}

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

#Use * and ** in function definitions to collect arguments, and use them in function calls to unpack arguments.
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")