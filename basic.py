
""""
x = 3
x= str(3)  #type casting
print(type(x))

x,y,z = "apple","cat","dog"
print(f"{x,y,z}")

#string
a = "data "
b = "is "
c= "oil "
print(f"{a + b + c}")

#error
a = str(20) 
b = 20
c= 30
print(f"{a + b + c}") 
    print(f"{a + b + c}")
             ~~^~~
TypeError: can only concatenate str (not "int") to str
# global
x = "data"
def func():
    global y
    y = "sachya"
    print("really",y)
func()
print(y)

#data types
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
# type func
x= 5
print(type(x))

x = ["apple", "banana", "cherry"]	#list
y = ("apple", "banana", "cherry")   #tuple
x1 = {"name" : "John", "age" : 36}   #dict
x2= {"apple", "banana", "cherry"}   #set
x3 = frozenset({"apple", "banana", "cherry"}) #frozenset

x4 = True	#bool
x5 = b"Hello" #bytes
x6 = bytearray(5) #bytearray
x7 = memoryview(bytes(5)) #memoryview
x9 = None #NoneType
z = range(6)  #range
print(x4)
