#!/usr/bin/env python
# coding: utf-8

# In[2]:


#question 1
def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result
list1 = [2, 3, 6]
print(multiplyList(list1))


# In[4]:


#question 2
from operator import itemgetter
a_list= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
a_list.sort(key=itemgetter(1))
print(a_list)


# In[5]:


#question 3
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d= Counter(d1)+Counter(d2)
print(d)


# In[6]:


#question 4
le_carré={}
n=int(input('enter un nombre'))
for i in range(1,n+1):
    le_carré[i]=i*i
print (le_carré)


# In[7]:


#question 5
a_list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
a_list.sort(key=itemgetter(1), reverse=True)
print(a_list)


# In[ ]:




