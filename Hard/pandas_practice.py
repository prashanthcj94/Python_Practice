import pandas as pd
import numpy as np


mydata = np.array([[1,3],[2,14],[3,18],[4,19],[12,44]])
mycolumnes = ['temperature', 'humidity']

df = pd.DataFrame(data=mydata,columns=mycolumnes)

print(df)

print(df.head(3))

print(df.iloc[[2]])


print(df[1:4])


column_names = ['cj','ice','jk','jp']
myd = np.random.randint(low=1,high=101,size=(3,4))

mydf = pd.DataFrame(data=myd,columns=column_names)

print(mydf)

print(mydf['ice'][1])

c = mydf.copy()
print(c)