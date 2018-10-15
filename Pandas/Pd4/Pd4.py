#Pandas Viwe VS Copy

import pandas as pd
import numpy as np


df= pd.DataFrame( {'user' : [1,2,3],
            'age' : [24,54,17],
            'sex' : ['F','F','M'],
            'occupation' : ['technician','musician','student']})
print(df)

# Part 1: Warning after failed attempt at setting values

# Suppose we want to change the values 'F' to 'Female'.

df[df.sex=='F'].sex = 'Female'

print("Trying to modify DF")
print(df)

print ("Correcting Warning of working with copy by using operator .loc while using a view of the DF")
df.loc[df.sex=='F','sex'] = 'Female'
print(df)

# ***************************************APPLYING FUNCTIONS *****************************************

print("Applying functions")

print("DF definition...")
df = pd.DataFrame( {'user' : [1,2,3], 'age' : [24,54,17],  'sex' : ['F','F','M'], 'occupation' : ['technician','musician','student']})
print(df)

# ***************************************** THE MAP METHOD () ***************************************************

# The method map() applies to Series and is used to REPLACE THE EXISTING VALUE IN A SERIES WITH DIFFERENT VALUES

print("The method map() applies to Series and is used to REPLACE THE EXISTING VALUE IN A SERIES WITH DIFFERENT VALUES")
print("Replacing F -> Female and M -> Male")
df['sex'] = df.sex.map({'F':'Female', 'M':'Male'})
print(df)

# *************************************** THE APPLY METHOD () ***************************************************

# The method apply() is both for Series and DataFrame. It is used for applying a function to each element of series

def dog_years(x):
    return x//7

print("The method apply() is both for Series and DataFrame. It is used for applying a function to each element of series")
print("Running function which is applied to all data in column age and converted into dog years")
df['age_dog_years'] = df['age'].apply(dog_years)
print(df)

print("************** Apply method example using numerical values ****************")

print("DF Definition...")
df2 = pd.DataFrame(np.arange(9).reshape(3,3), columns=['a','b', 'c'])
print(df2)

def my_sum(x):
    return sum(x)

print("Using method apply in the axis = 0")
print(df2.apply(my_sum, axis=0))

print("Using method apply in the axis = 1")
print(df2.apply(my_sum, axis=1))

# The nice thing about the apply() method is that we can not only use it with functions we defined ourselves, 
# but also with functions we have seen before from NumPy. Here are some examples:

print("Using already defined functions in the method apply()")
print("Numpy max number in axis 1")
print(df2.apply(np.max, axis = 1))
print("Numpy max number in axis 0")
print(df2.apply(np.max, axis = 0))

# The applymap() method
# The applymap() method is used to apply a function to every element of a DataFrame

def add_two(x):
    return x+2

print("The applymap() method is used to apply a function to every element of a DataFrame")
print(df2.applymap(add_two))
