# Unit 5 - Financial Planning

### Part 1 - Personal Finance Planner [//github.com/AkanSri/Rutgers-FinTech/blob/dbb7de38bfc477ff27412e4c1d10f3071ad53995/02-Homework/05-APIs/Starter_Code/#Part-1---Personal-Finance-Planner]

First, I created a personal finance planner that will allow users to visualize their savings composed by investments in shares and cryptocurrencies to assess if they have enough money as an emergency fund. I accomplished this by:
 * Collecting Crypto Prices Using the `requests` Library
 * Collecting Investments Data Using Alpaca for `SPY` (stocks) and `AGG` (bonds)
 * Computing the value in dollars of the current amount of shares 
 Then I assessed the financial health of the credit union's members by calculating the current savings by totaling the value in dollars of the crypto assets and shares. Then, setting a financial goal of three times their monthly income and comparing is to the total savings.

### Part 2 - Retirement Planning
I also created a retirement planning tool.
 * Using the Alpaca API to fetch historical closing prices for a retirement portfolio composed of stocks and bonds. 
 * Runs Monte Carlo simulations to project the portfolio performance at 30 years
 * Calculates the expected portfolio returns given a specific initial investment amount and the Monte Carlo data.

### Optional Challenge - Early Retirement
Using the retirement planning tool, I adjusted the portfolio to either include more risk (a higher stock than bond ratio) or to have a larger initial investment and reran the retirement analysis to see what it would take to retire in `5` or `10` years instead of `30`!
