#!/usr/bin/env python
# coding: utf-8

# In[18]:


print("CALCULator");
print("what arithematic to you want to perform between 2 numbers");


b=1;

while True:
 a=input("enter +-/*");
   
    
 if a=='+' :
    print("enter 1st number");
    x= input('1st value=')
    x=int(x)
    
    y= input('2nd value=')
    y=int(y)
    
    print('sum =')
    print(x+y)
    
 elif a=='-' :
    print("enter 1st number");
    x= input('1st value=')
    x=int(x)
    
    y= input('2nd value=')
    y=int(y)
     
   
    print('diff =')
    print(x-y)
    
 elif a=="*":
    print("enter 1st number");
    x= input('1st value=')
    y= input('2nd value=')
    x=int(x)
    
    y=int(y)
   
    print('product =')
    print(x*y)
     
 elif a=='/' :
    print("enter 1st number");
    x= input('1st value=')
    y= input('2nd value=')
    x=int(x)
   
    y=int(y)
    
    print('product =')
    print(x/y)
 else:
    print("invalid entry")
    continue
 print("do you want to do any calculation again, press 0 or 1")
 b=input("enter o or 1")
 b=int(b)
   
 if b==0:
    break


# In[ ]:




