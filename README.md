# calc
print("CALCULator");
print("what arithematic to you want to perform between 2 numbers");


b=1;

while True:
 a=input("enter +-/*");
   
    
 if a=='+' :
    print("enter 1st number");
    x= input('1st value=')
    x=int(x)
    if x.alpha():
     print("That's not an int!")
    continue
    y= input('2nd value=')
    y=int(y)
    if x.alpha():
     print("That's not an int!")
    continue
    print('sum =')
    print(x+y)
    
 elif a=='-' :
    print("enter 1st number");
    x= input('1st value=')
    x=int(x)
    if x.alpha():
     print("That's not an int!")
    continue
    y= input('2nd value=')
    y=int(y)
    if x.alpha():
     print("That's not an int!")
    continue
    print('diff =')
    print(x-y)
    
 elif a=="*":
    print("enter 1st number");
    x= input('1st value=')
    y= input('2nd value=')
    x=int(x)
    if x.alpha():
     print("That's not an int!")
    continue
    y=int(y)
    if userinput.alpha():
     print("That's not an int!")
    continue
    print('product =')
    print(x*y)
     
 elif a=='/' :
    print("enter 1st number");
    x= input('1st value=')
    y= input('2nd value=')
    x=int(x)
    if userinput.alpha():
     print("That's not an int!")
    continue
    y=int(y)
    if userinput.alpha():
     print("That's not an int!")
    continue
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
