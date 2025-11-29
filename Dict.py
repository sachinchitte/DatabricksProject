# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates
from operator import itemgetter

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'colors': ['red', 'white', 'blue']}
print(thisdict["brand"]) #Ford
print(len(thisdict)) #4

#The get() method returns the value of the item with the specified key.
# key required to pass but value	Optional in get(). A value to return if the specified key does not exist.
#Default value  None
#dictionary.get(keyname, value)
x=thisdict.get("year") #0/p 1964
x1=thisdict.get("years",123) #prints given value if key is not present #123
x1=thisdict.get("years") #prints None as default value if key is not present
print(x1)

#The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
print(x)
x = thisdict.values()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change
car["color"] = "red" #add new key and value
print(x) #after the change #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") #o/p "yes

#upadate
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict) #o/p {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

thisdict.pop("model")
print(thisdict) #o/p {'brand': 'Ford', 'year': 2020}

for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)

#Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y) #o/p brand Ford  year 2020

mydict = thisdict.copy()
