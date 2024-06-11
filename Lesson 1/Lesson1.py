### Lesson1.py ###
### Introduction to data types, variables, and operators

### Variables and Data Types ###

# At their most basic, variables store information in various data types

# Integers are whole numbers
myInteger = 13 

# Floats are numbers with a decimal
myFloat = 3.14159 

# Strings are text. Some programming languages also have a data type called a 'character' which represents a single letter
myString = "Hello World!" 

# Booleans are True or False 
myBoolean = True

### Operators ###

# Operators are signs which are used to "evaluate", or find out information from, variables, or to assign information to variables

## Assignment Operators ##

# The "=" operator has already been covered above

myInt = 0
myInt = myInt + 10
myInt += 10

print ("\nmyInt is equal to")
print (myInt)

# These are called "Compound Assignment" operators. They do an action on the current value of the variable.
# +=
# -=
# *=
# /=


## Inequality Operators ##

print ("\nIs 3 greater than 4?")
print(3 > 4) # Returns 'False' because 3 is not greater than 4

print ("\nIs 3 less than 4?")
print(3 < 4) # Returns 'True' because 4 is greater than 3

print ("\nIs 4 less than or equal to 4?")
print (3 <= 4) # Returns 'True' because 3 is less than or equal to 4

print ("\nIs 3 greater than or equal to 4?")
print (4 >= 4) # Returns 'True' because 4 is equal to to 4

print ("\nIs 10 greater than or equal to 4?")
print (10 >= 4) # Returns 'True' because 10 is greater than 4

## Equality Operators ##

print ("\nIs 3 equal to 4?")
print(3 == 4) # Returns 'False' because 3 is not equal to 4.
              # Notice that we use two equals signs, "==" not "=", as the equality operator. 
              # the single "=" is only used to assign data to a variable, also known as "defining" a variable

print ("\nIs 3 not equal to 4?")
print(3 != 4) # Returns 'True' because 3 is not equal to 4

### Getting User Input ###

# User input can be retrievd by using the input() method.
# Methods, also called functions, like the print() method run code that is written somewhere else.
# We will cover writing our own methods later.

myInput = input("\nWhat is your name? ")

print("Your name is " + myInput + "?")