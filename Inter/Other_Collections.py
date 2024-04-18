#Counter,namedTuple, Ordered Dict,Default Dict,  Deque

from collections import Counter
from collections import namedtuple
from collections import defaultdict
from collections import deque

a = "aaaaabbccccddduuu"


c = Counter(a)

print(c)            #prints each elements with counts
print(c.most_common())      #prints most common count
print(c.most_common(1)[0][0])       #accessing most common in tuple

print(list(c.elements()))           #printing as list of elements

point = namedtuple("point","x,y")
pt = point(1,-4)        #for declaring as points as named tuple
print(pt.x, pt.y)


def default():
    return "Not Present"
d = defaultdict(default)            #default values will be given when accesed
d['a'] = 1
d['b'] = 2
print(d['c'])


dq = deque()
dq.append("a")
dq.append("b")          #can deque from left and right ALSO Rotates.
print(dq)
dq.appendleft("c")
print(dq)
dq.popleft()
dq.rotate(1)
print(dq)



