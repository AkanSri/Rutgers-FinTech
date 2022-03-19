# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Sally
organize her grocery shopping list.
"""

# @TODO: Create a list of groceries
groceries = ["Water", "Butter", "Eggs", "Apples", "Cinnamon", "Sugar", "Milk"]
print(groceries)
# @TODO: Find the first two items on the list
print(groceries[0:2])

# @TODO: Find the last five items on the list
print(groceries[-5:])

# @TODO: Find every other item on the list, starting from the second item
print(groceries[1::2])

# @TODO: Add an element to the end of the list
groceries.append("flour")
print(groceries)

# @TODO: Changes a specified element within the list at the given index
groceries[groceries.index("Apples")]= "Gala Apples"
print(groceries)

# @TODO: Calculate how many items you have in the list
print(f"{len(groceries)}")

