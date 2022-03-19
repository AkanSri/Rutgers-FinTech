# -*- coding: utf-8 -*-
"""
Zero-Coupon Bond Valuation.

This script will calculate the present value of zero-coupon bonds, compare the present value to the price of the bond, and determine the corresponding action (buy, not buy, neutral).
"""

# @TODO: Create a function to calculate present value
def calculate_present_value(future_value, discount_rate, compounding_periods, years):
    """
    Calculates the present value of money given the future_value, interest rate, compounding period, and number of years.

    Args:
        future_value (float): The future value
        discount_rate (float): The discount rate
        periods (int): The compounding period
        years (int): The number of years

    Returns:
        The present value of money.

    """

    present_value =  future_value / ((1 + (discount_rate / compounding_periods))**(compounding_periods * years))
    present_value_formatted = round(present_value, 2)

    return present_value_formatted

price = 700
future_value = 1000
discount = .1
com_per = 1
yrs = 5

bond_value = calculate_present_value(future_value,discount,com_per,yrs)

print(f"Price: ${price} \nBond value: ${bond_value}")
if bond_value > price:
   print(f"Purchase the bond. Discount is ${round(bond_value - price,2)}")
elif bond_value < price:
   print(f"DO NOT purchase the bond. Premium is ${round(price-bond_value,2)}")
else:
   print("Bond is selling at its fair market value")















# Intialize the zero-coupon bond parameters, assume compounding period is equal to 1
price = 700
future_value = 1000
discount_rate = .1
compounding_periods = 1
years = 5

# @TODO: Call the calculate_present_value() function and assign to a variables


# @TODO: Determine if the bond is worth it
