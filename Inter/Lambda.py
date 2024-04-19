# lambda arguments : expression
# map( Func , seq )
# filter ( Func , seq )
#reduce ( Func , seq )
from functools import reduce


add = lambda x,y : x+y      #lambda add
print(add(3,7))

mul = lambda x,y : x*y      #lambda sub
print(mul(3,7))

p2D = [(5,1),(1,7),(3,-1),(-1,8)]
p2D_x_sort = sorted(p2D)            #sort in x value in points

print(p2D)
print(p2D_x_sort)

p2D_y_sort = sorted(p2D,key = lambda x : x[1])
print(p2D_y_sort)           #sort in y value in points

p2D_add = sorted(p2D, key = lambda x : x[0] + x[1])     #sort in addition of two points
print(p2D_add)

a = [1,2,3,4,5]
b = map(lambda x : x * 2,a)         # map maps each value
print(list(b))

c = [x*2 for x in a]        #easy way to do above
print(c)

m = [1,2,3,4,5,6]
f = filter(lambda x : x%2==0, m)        #filter used to filter out in list
print(list(f))

n = [x for x in m if x%2==0]        #easy way to do above
print(n)

o = [1,2,3,4]
prod = reduce(lambda x,y : x*y,o)       # reduce gets two args and gives single output
print(prod)