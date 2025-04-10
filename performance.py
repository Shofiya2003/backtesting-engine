import numpy as np
from pandas import Series


def calculate_total_return(final_portfolio_value: float, initial_capital: float):
    return (final_portfolio_value-initial_capital)/initial_capital

def calculate_annualized_return(total_return: float, days: int):
    return (1+total_return)**(252/days) - 1

def calculate_annualized_volatility(daily_returns: Series):
    return daily_returns.std() * np.sqrt(252)

def calculate_sharpe_ratio(annualized_returns: float, annualized_volatility: float):
    return annualized_returns/annualized_volatility

