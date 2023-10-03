import random


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
print("python is " + s,'\n') 

# Type Conversion

x = 1
y = 2.4
z = 5j

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)
print('\n')


#Import the random module, and display a random number between 1 and 9:
print(random.randrange(1, 10))
print('\n')

#casting
x = int(9)
y= int(2.3)
z= int("3")

print(x,y,z)

x=str('s1')
y=str("7")
z=str(3.4)

print(x,y,z)
print('\n')


# String as Arrays
a= "Hello World"
print(a[1],a[5],a[6])
print('\n')

#Looping through String
for x in "banana":
  print(x)

# String Length
a = "Hello, World"
print(len(a)) 
print("\n") 

# Check Text
txt = "The best thing are free"
print('free' in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)
print("\n") 

# Check Text with if
txt= "The best things are free"
if "free" in txt:
  print("ok boy")

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")