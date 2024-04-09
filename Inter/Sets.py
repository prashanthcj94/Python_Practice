#Sets are mutable and unordered and cannot contain duplicates

set1 = {1,2,3,2,1}      #way to declare a set {}
print(set1)

set2 = set([1,2,3,5,6,2,1])     #declare using set function
print(set2)
set3 = set("Prashanth")     #a trick to find unique characters in string
print(set3)


set1.add(4)
set1.add(5)         #element can be added using add

print(set1)

set1.remove(5)      #element can be removed by remove but error thrown if not present
print(set1)

set1.discard(5)     #element will be removed if present or not present
print(set1)

set2.clear()        #it will clear all elements
print(set2)

set1.pop()      #removes first element
print(set1)
set1.pop()
print(set1)

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}


print(odds.union(evens))        #unions two sets and doesnt affect the original set
print(evens.intersection(primes))       #intersects two sets

a = {1,2,3,4,5,6,7,8,9}
b={1,2,3,10,11,12}

print(a.difference(b))      #differences in A
print(b.difference(a))      #differences in B

print(a.symmetric_difference(b))        #differences in both A and B

a.update(b)         #upates two sets
print(a)

a = {1,2,3,4,5,6,7,8,9}
b={1,2,3,10,11,12}

a.intersection_update(b)        #updates with same elements in two sets
print(a)

a = {1,2,3,4,5,6,7,8,9}
b={1,2,3,10,11,12}

a.difference_update(b)      #updates with only differences in A
print(a)

a = {1,2,3,4,5,6,7,8,9}
b={1,2,3,10,11,12}
a.symmetric_difference_update(b) #updates with differences in both
print(a)

setA = {1,2,3,4,5,6}
setB = {1,2,3}
setC = {10,11}
print(setB.issubset(setA))      #finds whether B is subset of A
print(setA.issuperset(setB))        #finds whether A is superset of B

print(setA.isdisjoint(setC))        #finds whether A doesnt have any elements of B

fset = frozenset([1,1,3,4,5,7,2])       #This is an immutable set cannot be altered
print(fset)


