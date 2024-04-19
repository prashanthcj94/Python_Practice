# errors and Excpetions

# import somemodule       #Module not found error

# a = 5
# print(a))  # syntax error
#
# b = 5 + 'P'     # Type Error
#
# c = d  #name error
#
# o = open("somefile.txt")        #filenot found error
#
# a = [1,2,3]
# a.remove(4)     #value error
# a[4]        #index error
#
# a = {'name': 'cj'}
# print(a['age'])         #key error

# a = -5
# if a < 0:
#     raise  Exception("a should be positive")
#
# b = -5
# assert  (b>0),"b should be positive"


try:
    a = 5/0
except:
    print("an error happened")

try:
    a = 5/0
except Exception as e:
    print(e)


try:
    a = 5/0
    b = a + 's'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("everything is fine")
finally:
    print("Done and cleared")

class ValuetoohighError(Exception):
    pass
class ValuetoosmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value
def testvalue(x):
    if x > 100:
        raise ValuetoohighError("Value too high")
    if x < 100:
        raise ValuetoosmallError("Value too small", x)

try:
    testvalue(50)
except ValuetoohighError as e:
    print(e)
except ValuetoosmallError as e:
    print(e.message, e.value)