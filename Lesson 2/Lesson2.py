### Lesson2.py ###
### Introduction to String Manipulation & Type Casting ###

### Type Casting ###

# Python supports both "Implicit" and "Explicit" typing.
# When implicitly typing, Python will try to guess what data type is appropriate for the variable. 
# For example, if we say `myVar = 5` Python will read the 5 as an Integer data type and set it appropriately.

# However, sometimes we do not want the assumed data type that Python will use. 
# For example, when using the `input()` method, regardless of what is inputted on the Command Line Interface (CLI), 
# Python will store the value as a String. However, we can use "Type Casting" to "Explicitly" set the type to something
# like an Integer or Boolean


## int() ##

# The string that is being cast to an integer *MUST* be recognizably an integer, such as the numbers 0-9.
myInt = int(input("Please enter an Integer: "))
print(myInt + 1)

# The int() method can also be used to convert a float into an integer.
# When this is done, Python will "floor" or round-down the number to the nearest integer

print(int(6.98273)) # This will return 6

# The int() method can also be used to convert boolean True/False values to 1 or 0, respectively.

print(int(True)) # This will return 1


## float() ##

# The string that is being cast to a float *MUST* be recognizable a float, such as decimal numbers like 3.5 or 4.9
myFloat = float(input("Please enter a Float: "))
print(myFloat)

## str() ##

# It just converts whatever to a string

myString = str(89.6154) + "test"
print(myString)



### String Manipulation ###

## String Concatenation ##

# Concatenation is when you combine two strings into a single string.

myConcatenatedString = "Hello" + "World!"
print(myConcatenatedString)

# Notice that it will add them together *exactly* as they are written. 
# Formatting like spaces, tabs '\t', or new lines '\n' have to be added manually

myStringWithSpaces = "Hello " + "World!"
print(myStringWithSpaces)

## String Splitting ##

# You can split a string by telling Python which characters you want to print out
# Each character within a string has an index, or an ordered number, assigned to it
# In Python, like most programming languages, we count starting at 0, so the first
# character in a string is at index 0

myString = "Hello"
print(myString[2]) # This will print "e" because it is at the index 1.

# You can also use negative values to count backwards. 
# In the previous string the character at index -1 is "o"

print (myString[-1])

# You can also indicate any characters between two values by using the ":" character
# It will include the value to the left of the ":" and stop at the index one less than the value to the right

print (myString[1:3]) # This will print "el" as those character have the indices of 1, 2, and 3
print (myString[:2]) # This will print "He" because a blank before the ":" means we start at 0
print (myString[3:]) # this will print "lo" because a blank after the ":" means we end at -1

## String Methods ##

# count(value) # Returns the number of times a specified value occurs in a string
testString = "hello"
testString.count("l") # returns 2

# endswith(value) # Returns true if the string ends with the specified value
testString = "myFile.txt"
testString.endswith(".txt") # returns True

# find(value) # Searches the string for a specified value and returns the position of where it was found
testString = "myFile.txt"
testString.find("File") # returns 2

# index() # Searches the string for a specified value and returns the position of where it was found
testString = "myFile.txt"
testString.index(".") # returns 6

# len() # Returns the number of characters in a string
testString = "test"
len(testString) # returns 4

# lower() # Converts a string into lower case
testString = "TEST"
testString.lower() # returns "test"

# strip() # Returns a trimmed version of the string
testString = "   test   "
testString.strip() # returns "test"

# replace() # Returns a string where a specified value is replaced with a specified value
testString = "table"
testString.replace("able", "est") # returns "test"

# startswith() # Returns true if the string starts with the specified value
testString = "myFile.txt"
testString.startswith("myFile") # returns True

# upper() # Converts a string into upper case
testString = "test"
testString.upper() # returns "TEST"

## F Strings ##

# F strings are a way to simpify complex strings and dynamically include variables
# To create an f string, place a single, un-quoted, f character before your quotation marks.

myFString = f'This is an f string'
print (myFString)

# You can dynamically include variables within the f string by placing the variable name within curly brackets {}
# When you use variables in this way, you do not need to include the + operator

myName = "Cameron"
myGreeting = f'Hello {myName}'
print(myGreeting)