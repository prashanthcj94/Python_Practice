# These are some itertools for iterating through .

from itertools import product
from itertools import permutations
from itertools import combinations,combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count,repeat,cycle
import operator

a = [1,2,3]
b = [11,12,13]

prod = product(a,b)
print(list(prod))

prod1 = product(a,b,repeat=2)
print(list(prod1))

x = [1,2,3]
per = permutations(x)
print(list(per))

per1 = permutations(x,2)
print(list(per1))


j = [1,2,3]
comb = combinations(j,2)
print(list(comb))
combwr = combinations_with_replacement(j,2)
print(list(combwr))

m = [1,2,3]
n = [1,2,5,4,3]
acc = accumulate(m)
print(list(acc))
accm = accumulate(m,func = operator.mul)
print(list(accm))
accmax = accumulate(n,func=max)
print(list(accmax))


def smaller_than_3(x):
    return(x<3)
g = [1,2,3,4,5]
grp = groupby(g,key=smaller_than_3)
for key,value in grp:
    print(key,list(value))

persons = [{"name":"prashanth","age":26},{"name":"ice","age":26},{"name":"ranga","age":25}]
grpp = groupby(persons,key= lambda x:x["age"])
for key,value in grpp:
    print(key,list(value))


#
# for i in count(10):       #infinite count
#     print(i)

# for i in cycle([1,2,3]):      #infinite cycle
#     print(i)

# for i in repeat(1):           #infinite repeats
#     print(i)