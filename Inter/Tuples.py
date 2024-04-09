#Tuples are immutable and cannot be changed once declared

import sys
import timeit

myTuple = (4,2,7,8,"Dravid")        #one way to declare tuple
print(myTuple)

myTuple1 = ("Dravid",)          #another way to declare tuple
print(myTuple1)

myTuple2 = tuple([3,6,8,2])     #another way to declare tuple
print(myTuple2)

print(myTuple.count(7))     #prints count of element

print(myTuple.index(8))     #prints index of element

first,*second,third = myTuple       #splits according to index
print(first)
print(second)
print(third)
listdup = [4,2,1,7]
tupledup = (4,2,1,7)
print(sys.getsizeof(listdup))           #Differnce 1 - size is very small for tuple
print(sys.getsizeof(tupledup))

print(timeit.timeit(stmt="[2,5,4,2,4,5,7]",number=1000))
print(timeit.timeit(stmt="(2,5,4,2,4,5,7)",number=1000))    #Difference 2 - processing speed is very high for tuples



