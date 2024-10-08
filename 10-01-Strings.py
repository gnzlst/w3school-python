# Strings

# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# You can display a string literal with the print() function:
# Example
# Get your own Python Server
print("Hello")
print('Hello')
# Assign String to a Variable

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
# Example
# Get your own Python Server
a = "Hello"
print(a)
# Multiline Strings

# You can assign a multiline string to a variable by using three quotes:
# Example
# Get your own Python Server

# You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes:
# Example
# Get your own Python Server
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Note: in the result, the line breaks are inserted at the same position as in the code.
# Strings are Arrays

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.
# Example
# Get your own Python Server

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])
# Looping Through a String

# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Example
# Get your own Python Server

# Loop through the letters in the word "banana":
for x in "banana":
    print(x)

# Learn more about For Loops in our Python For Loops chapter.
# String Length

# To get the length of a string, use the len() function.
# Example
# Get your own Python Server

# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))
# Check String

# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Example
# Get your own Python Server

# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement:
# Example
# Get your own Python Server

# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Learn more about If statements in our Python If...Else chapter.
# Check if NOT

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# Example
# Get your own Python Server

# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

# Use it in an if statement:
# Example
# Get your own Python Server

# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")