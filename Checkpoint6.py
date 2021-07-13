#!/usr/bin/env python
# coding: utf-8

# In[8]:


#question 1
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
num_list = array_num.tolist()
print("list:", num_list)


# In[13]:


#question 2
import numpy as np
m = np.arange(6).reshape(2,3)
print(m)
result =  np.trace(m)
print("result:", result)


# In[14]:


#question 3
import numpy as np
x = np.array([[0, 10, 20], [20, 30, 40]])
print("Original array: ")
print(x)
print("Values bigger than 10 =", x[x>10])


# In[19]:


#question 4
import numpy as np
A = np.array([0, 1, 2])
B = np.array([5, 5, 5])
C = A+B
print(C)


# In[28]:


#question 5
import numpy as np
print("Original matrix:")
X = np.random.rand(1, 4)
print(X)
print("new matrix:")
Y = X - X.mean()
print(Y)


# In[ ]:




