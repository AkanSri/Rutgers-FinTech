# Percent Increase Bonus Activity

# Formulas
# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create float variable for original_price
original_price = float(input("Original Price:"))

# Create float variable for current_price
current_price = float(input("Current Price:"))

# Calculate difference between current_price and original_price
increase = current_price - original_price

# Calculate percent_increase
percent_increase = increase / original_price * 100

# Print original_price
print(f"Apple's original stock price was ${original_price}")

# Print current_price
print(f"Apples current stock price is ${current_price}")

# Print percent_increase to 2 decimal places using string formatting
print(f"The percent increase is % {round(percent_increase,2)}")