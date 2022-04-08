import numpy as np
'''
Calculates Sharpe ratio
Parameter(s): Input dataframe (returns_df)
Returns: Output dataframe (sharpe_ratios)
'''
def sharpe_ratio(returns_df):
    sharpe_ratios = returns_df.mean()*252/(returns_df.std()*np.sqrt(252))
    return (sharpe_ratios)

'''
Calculates cumulative returns
Parameter(s): Input dataframe (returns_df)
Returns: Output dataframe (cumulative_return)
'''
def cumulative_returns(returns_df):
    cumulative_return = (1 + returns_df).cumprod() - 1
    return (cumulative_return)

'''
Calculates cumulative returns
Parameter(s): Input dataframe(returns_std_df), boolean(calc_std) if std needs to be calculated
Returns: Output dataframe (ann_std)
'''
def annualized_std(returns_std_df, calc_std):
    if(calc_std):
        returns_std_df = returns_std_df.std()
    ann_std = returns_std_df * np.sqrt(252)
    return(ann_std)

'''
Calculates weighted Returns
Parameter(s): Input dataframe(returns_df), Initial investment(init_invest)
Returns: Output dataframe
'''
def weighted_portfolio_returns(returns_df, init_invest):
    w = 1/len(returns_df)    
    weights=[]
    for i in returns_df:
        weights.append(w)
    
    cumulative_ret = cumulative_returns(returns_df.dot(weights))
    returns = init_invest * cumulative_ret

    return returns

'''
pct_change() - sp500_history_data.pct_change()
std() - all_portfolios_returns.std()

Rolling 
- Standard deviation:
rolling_std_21 = all_portfolios_returns.rolling(window=21).std()

'''
