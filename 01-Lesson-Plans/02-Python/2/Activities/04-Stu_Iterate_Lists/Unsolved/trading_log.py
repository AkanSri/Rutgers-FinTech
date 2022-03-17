# -*- coding: utf-8 -*-
"""
Student Do: Trading Log.

This script demonstrates how to perform basic analysis of trading profits/losses
over the course of a month (20 business days).
"""

# @TODO: Initialize the metric variables
count = 0 
total = 0
avg = 0
minDay = 0
maxDay = 0

# @TODO: Initialize lists to hold profitable and unprofitable day profits/losses
profitableDays = []
unprofitableDays = []

# List of trading profits/losses
trading_pnl = [ -224,  352, 252, 354, -544,
                -650,   56, 123, -43,  254,
                 325, -123,  47, 321,  123,
                 133, -151, 613, 232, -311 ]

# @TODO: Iterate over each element of the list
for trade in trading_pnl:
    
    # @TODO: Cumulatively sum up the total and count
    total += trade
  
    # @TODO: Write logic to determine minimum and maximum values
    if minDay == 0:
        minDay = trade
    elif minDay > trade:
        minDay = trade
    elif maxDay < trade:
        maxDay = trade

    # @TODO: Write logic to determine profitable vs. unprofitable days
    if trade > 0:
        profitableDays.append(trade)
    else:
        unprofitableDays.append(trade)

# @TODO: Calculate the average
print (f"The average is {total/len(trading_pnl)}")

# @TODO: Calculate count metrics

print (f"The count is {len(trading_pnl)}")

# @TODO: Calculate percentage metrics
per_profitable = len(profitableDays)/len(trading_pnl)
per_unprofitable = len(unprofitableDays)/len(trading_pnl)

# @TODO: Print out the summary statistics

