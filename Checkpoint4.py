#!/usr/bin/env python
# coding: utf-8

# In[2]:


#question 1
def maximum(a,b,c):
    if a>=b and a>=c:
        largest= a
    elif b>=a and b>=c:
        largest= b
    else:
        largest= c
    return largest
maximum(94,91,95)


# In[4]:


#question 2
def calculation(a,b):
    return (a+b,a-b)
calculation(60,20)


# In[10]:


#question 3
l=[0,3,46]

def Sum(l):
    S=0
    for i in range (len(l)):
        S=S+l[i]
    return (S)
print ("total:",Sum(l))

def Multi(l):
    D=1
    for z in range (len(l)):
        D=D*l[z]
    return (D)
print ("product:",Multi(l))

o=[]
e=[]
for i in range(len(l)):
        if i%2==0:
            e.append(l[i])
        else:
            o.append(l[i])
print ("total²:",Sum(e))
print ("product²:",Multi(o))


# In[13]:


#question 4
ch=input('enter a list of caracters ')
def split_sort(items):
    items=[n for n in items.split('-')]
    items.sort()
    print('-'.join(items))
    return items
print (split_sort(ch))


# In[14]:


#question 5
import math
numbers=input("provide D:")
numbers=numbers.split(',')
result_list = []
C=50
H=30
def calculate(D):
    Q= round(math.sqrt(2 * C * int(D)/H))
    return Q
for i in numbers:
    Q=calculate(i)
    result_list.append(Q)
print(result_list)


# In[ ]:




