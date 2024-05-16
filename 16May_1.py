#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Student:
    def __init__(self, fee):
        self.fee=fee
        
    @property
    def convert(self):
        return  self.fee*80

s1=Student(100)
s1.convert


# In[21]:


class Student:
    def __init__(self, fee):
        self.fee=fee
     
    @staticmethod
    def convert(x,y):
        return  x+y


Student.convert(10,20)


# In[33]:


class Dollar:
    def __init__(self, amount):
        self.amount=amount
        
    def __repr__(self):
        return f"Dollar class has values {self.amount}"
    
    @classmethod
    def convert(cls,x,y):
        return cls(x-y)
    

class Euro(Dollar):
    def __init__(self, amount):
        super().__init__(amount)
        
    def __repr__(self):
        return f"Euro class has {self.amount}"
    
e1=Euro(90)
e1.convert(60,50)

d1=Dollar(909)
d1.convert(160,150)


# In[ ]:


# function
# lambda 
# list + tuple
# dictionary
# class object
# polymorh
#__init__
# self
# MRO
# __new__ ()   => instance banana

