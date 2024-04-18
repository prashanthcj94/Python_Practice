# String are Immutable, ordred

str1 = "i'm Prashanth Kumar"        #single quotes in double quotes
print(str1)

if "P" in str1:             #checks whether character is present
    print("Yes!!!")

for i in str1:
    print(i)


str2 = "    God Dammn   "       #strips unwanted spaces
print(str2)
str2 = str2.strip()
print(str2)

str1 = str1.lower()
print(str1)
print(str1.upper())         #lower and upper cases

print(str1.startswith("i'm"))
print(str1.endswith("kumar"))           #startswith and endswith funtions

print(str1.find("p"))
print(str1.count("a"))              #find and count function

print(str1.replace("i'm","Hello"))          #finds and replace char and strings

li = str1.split(" ")
print(li)                   #string to list and list to string
print("".join(li))
print("-----".join(li))

input1 = 1000101
list1 = str(input1)
print(list1[2])

a= "prashanth"
b = 98.9999999
print("Hi i'm %s" % a)
print("Hi i'm {} and i scored {:.1f}".format(a,b))             #Formating
print(f"Hi i'm {a} and i scored {b}")

