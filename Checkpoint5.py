#!/usr/bin/env python
# coding: utf-8

# In[1]:


#question 1
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def affiche(self):
        return (self.x, self.y, self.z)
        
my_point = Point3D(1,2,3)
t=my_point.affiche()
print("tuple:",t)


# In[2]:


#question  2
class Rectangle(object):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def aire(self):
        a=(self.length*self.width)
        return a
    def périmètre(self):
        p=(2*(self.length+self.width))
        return p
my_rectangle = Rectangle(4,3)
ta=my_rectangle.aire()
print ("aire:",ta)
tp=my_rectangle.périmètre()
print ("périmètre:",tp)


# In[3]:


#question 3
r=int(input("rayon du cercle: "))
x=int(input("x du cercle: "))
y= int(input("y du cercle: "))
O=(x,y)
x_A= int(input("x de A: "))
y_A= int(input("y de A: "))
A= (x_A,y_A)
from math import pi
from math import sqrt
class Circle():
    def __init__(self, O, r):
        self.center= O
        self.radius= r
    def area(self):
        return(pi*self.radius**2)
    def perimeter(self):
        return(2*pi*self.radius)
    def isInside(self,A):
        Q= sqrt((A[0]-self.center[0])**2+(A[1]-self.center[1])**2)
        if Q==r:
            return("A est sur le Cercle")
        elif Q<r:
            return("A est dans le Cercle")
        else:
            return("A est à l'extérieur du Cercle")
          
mon_cercle = Circle(O, r)
a=mon_cercle.area()
pe=mon_cercle.perimeter()
print("area is:", a)
print("perimeter is: ", pe)
mon_cercle.isInside(A)


# In[4]:


#question 4
class Bank:
    def __init__(self, balance):
        self.balance=balance
    def deposit(self, gain):
        self.balance = self.balance+gain
        return self.balance
    def withdraw (self,perte):
        self.balance=self.balance-perte
        return self.balance
x=int(input("valeur initiale: "))
balance_=Bank(x)
y=int(input("gain: "))
z=int(input("perte: "))      
print(balance_.deposit(y))
print(balance_.withdraw(z))


# In[ ]:




