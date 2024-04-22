import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

print(os.getcwd())

dataset = pd.read_csv('C:\\Users\\prashanth.k.lv\\Documents\\Python_Practices\\Resource\\student_scores.csv')

print(dataset)

print(dataset.shape)
print(dataset.head())
print(dataset.tail())
print(dataset.describe())

print(dataset.plot(x='Hours', y='Scores', style='o'))
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values

print(X)
print(Y)