# -*- coding: utf-8 -*-
"""Student Activity: Financial Analysis using NPV.

This script will choose the optimal project scenario to
undertake based on max NPV values.
"""

# @TODO: Import the NumPy Financial (numpy_financial) library
import numpy
import numpy_financial as npf

# Discount Rate
discount_rate = .1

# Initial Investment, Cash Flow 1, Cash Flow 2, Cash Flow 3, Cash Flow 4
cash_flows_conservative = [-1000, 400, 400, 400, 400]
cash_flows_neutral = [-1500, 600, 600, 600, 600]
cash_flows_aggressive = [-2250, 800, 800, 800, 800]

# @TODO: Initialize dictionary to hold NPV return values
npv_dict = {}

# @TODO: Calculate the NPV for each scenario
npv1 = npf.npv(discount_rate, cash_flows_conservative)
npv2 = npf.npv(discount_rate, cash_flows_neutral)
npv3 = npf.npv(discount_rate, cash_flows_aggressive)

# @TODO: Initialize variables
npv_dict = {"conservative": npv1, 
           "neutral": npv2, 
           "aggressive": npv3}

max_val = 0
max_key = ""
# @TODO: Iterate over npv_dict to find the max key-value pair
for k,v in npv_dict:
    print(f"{k}:{v}")
    if v > max_val:
        max_val = v
        max_key = k

print (f"The optimal project scenario to undertake is '{max_key}' with a NPV of{max_val}")
    
    









# @TODO: Print out the optimal project scenario with the highest NPV value
