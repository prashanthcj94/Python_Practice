#Dictionaries are mutable , unordered , key-value pairs

d1 = {"name": "cj","age": 26,"city":"Chennai"}      #one way to create dictionary
print(d1)

d2 = dict(name="ice", age=26,city="Chennai")            #another way to instantiate a dictionary
print(d2)

d1["email"] = "cj@gmail.com"        #if not present it will be added
print(d1)
d1["email"] = "icecj@gmail.com"     #if present it will get updated
print(d1)

del d1["email"]   #using delete command to remove
print(d1)

d2.pop("city")      #will remove with particular key
print(d2)

d1.popitem()        #will remove last element
print(d1)


if "name" in d1:
    print(d1["name"])       #searches with key

try:
    print(d1["age"])    #using try except
except:
    print("Error")

for keys in d1.keys():      #retrives all keys
    print(keys)
for values in d1.values():      #retrives all values
    print(values)
for key,value in d1.items():        #retrives all key and values
    print(key,value)


copyd1 = d1.copy()      #best copy way
print(copyd1)
copyd2 = dict(d2)       #another copy way
print(copyd2)

d1["city"] = "Chennai"
d2["email"] = "ice@gmail.com"
d1.update(d2)       #it will get updated with second dictionary
print(d1)

d1[72] = 94
print(d1[72])       #immutable types can be used as keys

d1[(8,7)] = 15      #even tuples are immutable so it can be used
print(d1)
print(d1[(8,7)])



