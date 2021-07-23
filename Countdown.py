#!/usr/bin/env python
# coding: utf-8

# In[9]:


import time

t = input("Enter the time in seconds: ")

def countdown(t):  
    t= int(t)
   
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Fire in the hole!')
  
countdown(int(t))


# In[ ]:




