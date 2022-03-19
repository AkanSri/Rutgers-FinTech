# -*- coding: utf-8 -*-
"""Student Do: E-Commerce Traffic.

This script will parse through a text file and sum the total
number of customers and the count of days in the text file to
calculate the daily average of customer traffic for an e-commerce
business.
"""

# @TODO: From the pathlib library, import the main class Path
from pathlib import Path

# @TODO: Check the current directory where the Python program is executing from
print(f"Current working dir: {Path.cwd()}")

# @TODO: Set the path using Pathlib
filepath = Path("/Users/akanksha/Rutgers/Rutgers-FinTech/01-Lesson-Plans/02-Python/3/Activities/08-Stu_File_IO/Resources/customer_traffic.txt")

# Initialize variables
customer_total = 0
day_count = 0

# @TODO: Open the file in "read" mode ('r') and store the contents in the variable 'file'
with open (filepath,'r') as file:
    # @TODO: Parse the file line by line
    for line in file:
        # @TODO: Convert the number in the text file from string to int (allows for numerical calculations)
        number = int(line)
        # @TODO: Sum the total and count of the numbers in the text file
        customer_total += number
        day_count +=1

# @TODO: Print out customer_total and day_count
print(f"customer_total: {customer_total} \n day_count: {day_count}")

# @TODO: Calculate the average
daily_avg = customer_total/day_count
print(f"daily_avg: {daily_avg}")
# @TODO: Set output file name
output_path = "Rutgers-FinTech/01-Lesson-Plans/02-Python/3/Activities/08-Stu_File_IO/output.txt"

# @TODO: Open the output path as a file object
with open(output_path,"w") as file:
    # @TODO: Write daily_average to the output file, convert to string
    file.write(f"The total and count of the numbers in the text file are {customer_total} and {day_count}, respectively. The average is {daily_avg}.")