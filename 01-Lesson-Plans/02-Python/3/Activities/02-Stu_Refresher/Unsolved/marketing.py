# -*- coding: utf-8 -*-
"""Refresher activity.

This script will use variables, conditionals, lists, dicts, and functions
to print out different greetings for customers based on their
business tier (determined by revenue).
"""

# List of dicts
customers = [
    { "first_name": "Tom", "last_name": "Bell", "revenue": 0 },
    { "first_name": "Maggie", "last_name": "Johnson", "revenue": 1032 },
    { "first_name": "John", "last_name": "Spectre", "revenue": 2543 },
    { "first_name": "Susy", "last_name": "Simmons", "revenue": 5322 }
]

# @TODO Define a function that accepts a customer first_name, last_name, and
# revenue and returns a custom greeting with the full name.
# Use these ranges to determine the business tier (and corresponding message)
# for each customer.
#   Platinum = 3001+
#   Gold = 2001-3000
#   Silver = 1001-2000
#   Bronze = 0-1000
def create_greeting(first_name, last_name, revenue):
    # @TODO: YOUR CODE HERE!
    member = ""
    if revenue >= 3001:
        member = "PLATINUM "
    elif revenue >=2001 and revenue <= 3000:
        member = "GOLD "
    elif revenue >=1001 and revenue <= 2000:
        member = "SILVER "
    elif revenue >=0 and revenue <= 1000:
        member = "BRONZE "

    greeting = f"Thank you {first_name} {last_name} for your business of ${revenue}. You are a {member} member! "
    return greeting

# @TODO: Loop through the list of customers and use your function to print
# custom greetings for each customer.
# @TODO: YOUR CODE HERE!
for cust in customers:
    print(create_greeting(cust["first_name"],cust["last_name"],cust["revenue"]))
