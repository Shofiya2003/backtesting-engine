import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas import Series


def calculate_total_return(final_portfolio_value: float, initial_capital: float):
    return (final_portfolio_value-initial_capital)/initial_capital

def calculate_annualized_return(total_return: float, days: int):
    return (1+total_return)**(252/days) - 1

def calculate_annualized_volatility(daily_returns: Series):
    return daily_returns.std() * np.sqrt(252)

def calculate_sharpe_ratio(annualized_returns: float, annualized_volatility: float):
    return annualized_returns/annualized_volatility

def compare_with_buy_hold(buy_hold_daily_returns: pd.Series, strategy_returns: pd.Series):
    # buy_hold_daily_returns = buy_hold_daily_returns.sort_index()
    # strategy_returns = strategy_returns.sort_index()
    ((1 + buy_hold_daily_returns).cumprod()*10000).plot(label="Buy & Hold", color='blue')
    ((1 + strategy_returns).cumprod()*10000).plot(label="Strategy", color='red')
    plt.tight_layout()
    plt.legend()
    plt.show()
