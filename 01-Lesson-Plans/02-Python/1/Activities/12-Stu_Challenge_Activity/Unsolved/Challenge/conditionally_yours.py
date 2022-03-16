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

# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create integer variable for original_price
original_price = int(input("Original Price:"))

# Create integer variable for current_price
current_price = int(input("Current Price:"))

# Create float for threshold_to_buy
threshold_to_buy = float(input("Threshold to Buy:"))

# Create float for threshold_to_sell
threshold_to_sell = float(input("Threshold to Sell:"))

# Create float for portfolio balance
balance = float(input("Portfolio Balance:"))

# Create float for balance check
balance_check = balance * 5

# Create string for recommendation, default will be buy
recommendation = "buy"

# Calculate difference between current_price and original_price
increase = current_price - original_price

# Calculate percent increase
percent_increase = (increase / original_price) * 100

# Print original_price
print(f"Netflix's original stock price was ${original_price}")

# Print current_price
print(f"Netflix's current stock price is ${current_price}")

# Print percent increase
print(f"Netflix's stock price changed by{round(percent_increase,2)}%")


# Determine if stock should be bought or sold
if percent_increase >= threshold_to_sell:
    recommendation = "sell"
elif percent_increase <= threshold_to_buy:
    recommendation = "buy"
else:
    print("Not enough activity to warrant buy or sell action")

# Print recommendation
print("Recommendation: " + recommendation)
print()
print("But wait a minute... lets check your excess equity first.")


# Challenge

# Declare balance_check variable
balance_check = balance * 5

# Compare balance to recommendation, checking whether or not balance is 5 times more than current_price
print(f"You currently have ${balance} in excess equity available in your portfolio.")

# IF-ELSE Logic to determine recommendation based off of balance check
if ( recommendation == "buy" and balance_check >= current_price):
   recommendation = "buy"
print("Recommendation: " + recommendation)
