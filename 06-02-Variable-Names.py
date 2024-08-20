# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

#     A variable name must start with a letter or the underscore character
#     A variable name cannot start with a number
#     A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#     Variable names are case-sensitive (age, Age and AGE are three different variables)
#     A variable name cannot be any of the Python keywords.

# The Google Python Style Guide has the following convention:
# module_name
# package_name
# ClassName
# method_name
# ExceptionName
# function_name
# GLOBAL_CONSTANT_NAME
# global_var_name
# instance_var_name
# function_parameter_name
# local_var_name

# Example
# Get your own Python Server

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Example
# Get your own Python Server

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Remember that variable names are case-sensitive

# Multi Words Variable Names

# Variable names with more than one word can be difficult to read.

# There are several techniques you can use to make them more readable:
# Camel Case

# Each word, except the first, starts with a capital letter:
myVariableName = "John"
# Pascal Case

# Each word starts with a capital letter:
MyVariableName = "John"
# Snake Case

# Each word is separated by an underscore character:
my_variable_name = "John"

print(myVariableName)
print(MyVariableName)
print(my_variable_name)