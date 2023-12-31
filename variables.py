#python has no command for declaring variables
#a variable is created the moment you assign a value to it.

x='john'
y=5
print(x)
print(y)

#variables in python do not need to be declared with a particular type and...
# can even change type after they've been set 

x=4 #x is of type int
print(x)
x='sally' #x is of type string
print(x)

#specifying a data type of a variable is done through casting
x=str(3) # x will be '3'
print(x)
x=int(3) # x will be 3
print(x)
x=float(3) # x will be 3.0g 
print(x)

#you can get the type of variable by using the type() function
x=5
y="john"
print(type(x))
print(type(y))

#strings can be declared by using either single or double quotes

x ='john'
#same as
x="john"

#variable names are case sensitive

a=4
A="sally"
# 'A' will not overwrite 'a'


