"""
This file demonstrates some "Pythonic" style code you may encounter
- Run the code and examine the output
- Read the comments, search for the answers.
- Then modify the code to test it, see if you can predict the behavior!

"""

# C: Try changing "someList" so that "newList" has no even values
#
someList = [1, 0,5,6,4,3,9]

# C: What is a lambda function?
# C: What is the map function?
# C: What type does the map function return?
# C: What does the list() function do?
#
newList = list(map(lambda x : x**2, someList))

print(newList)

# C: Below is an example of a Ternary Expression.
#    Create your own Ternary Expression that checks
#    if newList is a list. Save a boolean in a variable
#    named isList and print it
#
hasOne = True if 1 in newList else False

# C: Convert print statement below to use fstring
print("hasOne: " + str(hasOne))

# C : What is a list comprehension?
# C : What is the modulus operator?
evenList = [
    x for x in newList if x % 2 == 0
]

print("Even List: " + str(evenList))
