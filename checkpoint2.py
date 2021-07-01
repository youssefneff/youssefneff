#!/usr/bin/env python
# coding: utf-8

# In[3]:


#question 2
a = int(input("input an integer:"))
n1 = int( "%s" % a)
n2 = int( "%s%s" % (a,a))
n3 = int( "%s%s%s" % (a,a,a))
print(n1+n2+n3)


# In[4]:


#question 3
num = int(input("enter a number:"))
mod = num % 2
if mod > 0:
    print("this is an odd number.")
else:
    print("this is an even number.")


# In[5]:


#question 4
nl=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print(','.join(nl))        


# In[6]:


#question 5
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Input a number to compute the factorial:"))   
print(factorial(n))


# In[ ]:




