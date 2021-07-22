#!/usr/bin/env python
# coding: utf-8

# In[10]:


#1
python_file=open ("python.txt", "r")
print (python_file.read())
python_file.close()


# In[8]:


#2
a_file = open("python.txt")
print(a_file.readline())
a_file.close()


# In[9]:


#3
file=open("python.txt", "r")
first_line = file.readline()
for last_line in file:
    pass
print(last_line)
file.close()


# In[11]:


#4
file = open("python.txt", "r")
d = file.read()
words = d.split()
print('Number of words in text file :', len(words))
file.close()


# In[12]:


#5 
file=open("python.txt", "r")
first_line = file.readline()
for last_line in file:
    pass
print(last_line)
file.close()


# In[ ]:





# In[ ]:




