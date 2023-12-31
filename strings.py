#Strings in python are surrounded by either single quotation marks, or double quotation marks.

#'hello' is the same as "hello".

#You can display a string literal with the print () function

print("Hello")
print('Hello')

#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)

#You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
#Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1])


#Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
  print(x)

#To get the length of a string, use the len() function.  
a = "Hello, World!"
print(len(a))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)