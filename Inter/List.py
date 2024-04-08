myList = ["prashanth","ishwarya","jimmy"]
print(myList)

list2 = list()     #cretes empty list
print(list2)
print(len(myList))      #gives len of list

myList.append("jackyy")     #adds new element to the last
print(myList)
myList.insert(2,"Tommy")        #adds new element to particular index
print(myList)

item = myList.pop()         # Removes last element
print(item)

myList.remove("Tommy")      #removes particular value
print(myList)

myList.reverse()        # reverses the list
print(myList)

myList.clear()      #clear's all element
print(myList)

list3 = [3,6,1,3,2,5,7,9]
list3.sort()        #sorts the list
print(list3)

copy = sorted(list3)        #creates new copy of list sorted
print(copy)

newList = [0]*5
print(newList)  #copies repetition

newList2 = [3,4,2,1,1,5]
a = newList2[::2]       #step wise
print(a)

b = newList2[::-1] #reverses
print(b)

copyOfNewlist2 = list(newList2)
copy3 = newList2.copy()         #all creates copy
copy4 = newList2[:]

print(copy4)

square = [i*i for i in newList2]  #includes squuare
print(square)