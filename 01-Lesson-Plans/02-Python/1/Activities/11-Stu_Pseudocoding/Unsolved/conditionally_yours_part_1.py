"""
Conditionally Yours
Pseudocode:

Formulas:
Increase = Current Price - Original Price
Percent Increase = Increase / Original x 100

Assumption: 
20% increase or decrease in stock price should warrant buy or sell action
If Percent Increase >=20 sell, else if buy Percent Increase <=-20 buy
"""
# Create float variable for original_price
original_price = float(input("Original Price:"))

# Create float variable for current_price
current_price = float(input("Current Price:"))

# Calculate difference between current_price and original_price
increase = current_price - original_price

# Calculate percent_increase
percent_increase = increase / original_price * 100
print( f"Percent Increase: {percent_increase}% ")

if percent_increase >= 20:
    print("Buy!")
elif percent_increase <= -20:
    print("Sell!")
else:
    print("Not enough activity to warrant buy or sell action")