#identation
if 5 > 2:
   print("Five is greater than two")
#variables
userage = 100
username= "joseph"
print(userage)
print(username)
#types of variables
myVariablename= "carel case joseph"
MyVaribleName="pascal case joseph"
my_variable_name= "snake case joseph"
print(myVariablename)
print(MyVaribleName)
print(my_variable_name)
#print function
x = "My Name is Andrew, First of his Name, Ruler of Egypt, Leader of the universe"
print(x)

a="joseph"
b="is"
c="cool"
print(a,b,c)
digit = b
digit = 5
print(digit)
print(type(digit))
#data types
digit2 = 1.5
print(digit2)
print(type(digit2))

digit3 =2j
print(digit3)
print(type(digit))
#random libary
import random
print(random.randrange(1,100))

# casting
# intergers
y = int ("1")
z = int (1.5)
t = int ("1")
print(type(y))
print(type(z))
print(type(t))
# float
b = float(1)
c = float(2.0)
d= float("3")
e = float("4.0")
print(type(b))
print(type(c))
print(type(d))
print(type(e))
#string
f = str(1)
g = str(1.0)
print(type(f))
print(type(g))

#strings
string1 = "i am the strongest,the brightest,the most awesome teacher in the world"
print(string1)
print(type(string1))
#concatenation
string2 = "he also a superhero - spiderman"
string3 = string1+string2
print(string3)

#python booleans
digit4 = 10
digit5 = 50
if digit5 > digit4:
    print("dijit 5 is more than dijit 4")
else:
   print ("digit 5 is more than dijit 4")
#arithmetic operators
#sum
h = 20
i = 30
j = h+i
print(j)
#substariction
k = i-h
print(k)
#multiplication
l = h*i
print(l)
#divison
m = i/h
print(m)
#modulus
n = 1%h
print(n)
#list
thislist = ["Apple","Banana","Cherry","Mango","Avocado"]
print(thislist)
#Accesslists
print(thislist[0])
#NegativeIndexing
print(thislist[-1])
#Rangeofindexes
print(thislist[1:4])


#whileloop
o = 1
while o < 6:
    print(o)
    o+=1

#breakstatement
p = 1
while p <6:
    print(p)
    if p==3:
        break
    p+=1

#else statement
q = 1
while q <6:
    print(q)
    q+=1
else:
    print("q is more than one")

#forloops
cars = {"Toyota,""suburu,""volkswagon,""nisssan,""buggati" }
for x in cars:
    print(x)
#functions
def myfunction():
    print("This is a function")
myfunction()

#INPUT
name = input("what is your name:")
print("your name is:" +name )





















