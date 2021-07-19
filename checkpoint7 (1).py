#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

my_array  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(my_array , index=labels_array)
print(df)
my_array= pd.DataFrame (mydict)
my_array.index=labels_array
print(my_array)
#question1
print("this is the 3 first rows of your dataframe:")
print(my_array.head(3))
#question2
print("this is your new dataframe:")
print(my_array.dropna())
#question3
print("this is the 2columns name and score:")
print(my_array.loc[:,('name','score')])
#question4
df.loc['k'] = [1, 'Suresh', 'yes', 15.5]
print("Print all records after insert a new record:")
print(df)
print("\nDelete the new row and display the original  rows:")
df = df.drop('k')
print(df)
#question5
print("this is your new dataframe:")
print(my_array.drop('attempts',axis=1))
#question6
array_score=my_array.loc[:,('score')]
list_add=[]
for i in array_add :
    if i>10:
        list_add.append(1)
    else: list_add.append(0)
my_array['Success']=list_add
print("this is your new dataframe:")
print(my_array)
#question7
my_array.to_csv('my_data')


# In[ ]:




