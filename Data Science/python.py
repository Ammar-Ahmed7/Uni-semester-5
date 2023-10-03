
#variables
a=30
b=200
c="Boy"
s="awesome"

#if condition(indentation important)
if b>a:
 print("b is greater than a")

#for multiline comment you can use string literals 
"""
this is multiline comment in a sense
"""
#printing values of variables
x="john"
y=87
print(x)
print(y)
print("\n")

#casting
p=str(4)
y=int(4)
t=float(4)
print(p,y,t)
print("\n")

#getting type
print(type(x))
print(type(y))
print("\n")

#Case sensitive
n=65
N="man"
print(n)
print(N)
print("\n")
#A will not overwrite a

#Many Values to Multiple Variables
f,g,h= "Orange", "Banana", "Cherry"
print(f)
print(g)
print(h)
print("\n")

#One Value to Multiple Variables
j = k = l="monkey"
print(j)
print(k)
print(l)
print("\n")

#Unpack Collection (values in a list to variables)
fruits = ['apple','banana','cherry']
q,w,e=fruits
print(q)
print(w)
print(e)
print("\n")

#Output variables
i="python is good"
print(i,"\n")

t=5
y=6
print(t+y,'\n')



#Global variables

def myfunc():
  print("pyton is " + s,'\n')

myfunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

def myfunc():
  s="fantastic"
  print("pyton is " + s)

myfunc()
print("pyton is " + s,'\n')

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global s
  s="Wow"

myfunc()  
print("python is " + s) 



