# Forecasting Net Prophet
MercadoLibre is the most popular e-commerce site in Latin America. As a growth Analyst, I've been tasked with analyzing the company's financial and user data in clever ways to help the company grow. So, I want to find out if the ability to predict search traffic can translate into the ability to successfully trade the stock. To do so, I created a Jupyter notebook that can be found in: : [Starter_Code/forecasting_net_prophet.ipynb](Starter_Code/forecasting_net_prophet.ipynb).

## Step 1: Find Unusual Patterns in Hourly Google Search Traffic
The data science manager asks if the Google search traffic for the company links to any financial events at the company. Or, does the search traffic data just present random noise? To answer this question, I connected the Google search data for the company to the corporate financial events to see if there are nay unusual patterns. Specifically, I looked at May 2020 when MercadoLibre released its quarterly financial results. <br>
First, I plotted the Google Search trends for May 2020 <br>
![Google_Search_Trends_May_2020.png](Images/Google_Search_Trends_May_2020.png)<br>
Then I calculated the total search traffic for May 2020 (which was 38181) and compared it to the monthly median across all months (which equals 35172.5). ***Therefore, there was an increase of 3008.5 searches in May 2020.*** <br>

## Step 2: Mine the Search Traffic Data for Seasonality
Marketing realizes that they can use the hourly search data, too. If they can track and predict interest in the company and its platform for any time of day, they can focus their marketing efforts around the times that have the most traffic. This will get a greater return on investment (ROI) from their marketing budget. To that end, I mined the search traffic data for predictable seasonal patterns of interest in the company. <br>
To do so, first I plotted the average traffic by the day of week<br>
![Avg_Traffic_Day.png](Images/Avg_Traffic_Day.png)<br>
Then, I visualized the data as a heatmap to be able to decide that: ***there seems to be more concentrated number on On Day 1 of the week, at hour 0 and Day 0 at hour 24. Then on Days 2-4 there is also a higher number at hour 0. Also, Day 1 and 2 at hour 24.***  <br>
![Heatmap_Trends_Hour_Day.png](Images/Heatmap_Trends_Hour_Day.png)<br>
I also grouped and plotted the data the average traffic by the week of the year to see if the search traffic tends to increase during the winter holiday period (weeks 40 through 52). ***Looking at the graph, it looks like the traffic dips down and slowly increases. But the highest traffic is towards the beginning of the year (weeks 2-8)***
![Avg_Traffic_Week.png](Images/Avg_Traffic_Week.png)<br>

## Step 3: Relate the Search Traffic to Stock Price Patterns
The finance group at the company also wants to know if any relationship exists between the search data and the company stock price. To determine if there is, I plotted both data sets to determine that ***in both time series there is a major dip in March, but there doesnt seem to be a similar increase in search trends as there is in the close price.***
![Search_2020.png](Images/Search_2020.png) <br>
![Close_2020.png](Images/Close_2020.png) <br>
To determine if there is a predictable relationship between the lagged search traffic and the stock volatility or between the lagged search traffic and the stock price returns, I first calculated the Stock Volatility using the standard deviation of the closing stock price return data over a 4 period rolling window. I also got the Hourly Stock Return by calculating the hourly return percentage of the closing price. Then I created a correlation matrix:
![Corr_table.png](Images/Corr_table.png) <br>
***Since these correlation numbers are so low, I don't think a predictable relationship exists between them.*** <br>

## Step 4: Create a Time Series Model with Prophet
I then used a Prophet forecasting model that analyzes and forecasts patterns in the hourly search data. The resulting forecasts plot:<br>
![forecast_mercado_trends.png](Images/forecast_mercado_trends.png) <br>
***So this shows, in near-term forecast, there is a steady decline and then slight rise at the end for the popularity of MercadoLibre*** <br>

After visualizing the forecast results, I was able to determine: <br>
    - ***The time of day that exhibits the greatest popularity is Midnight*** <br>
    - ***The day of the week that gets the most search traffic is Tuesday*** <br>
    - ***The lowest point for search traffic in the calendar year is towards the end of September.*** <br>
![forecast_trends_components.png](Images/forecast_trends_components.png) <br>

## Step 5 (Optional): Forecast Revenue by Using Time Series Models
The finance group wants a forecast of the total sales for the next quarter. First I used another Prophet forecasting model and analyzed the results to determine ***the peak revenue days are Mondays and Wednesdays, with Wednesday being the highest.*** <br>
![figures_sales_components.png](Images/figures_sales_components.png) <br> 
Then, using yhat as the Most Likely total sales for the next quarter, yhat_upper as the Best Case, and yhat_lower as the Worst Case, I was able to sum up the predictions for the quarter to determine: <br>
    - ***Most Likely: 969.577023*** <br>
    - ***Best Case: 1051.120123*** <br>
    - ***Worst Case: 887.214402*** <br>