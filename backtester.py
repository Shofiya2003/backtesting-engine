from typing import Dict

import pandas as pd
from matplotlib import pyplot as plt

from performance import calculate_total_return, calculate_annualized_return, calculate_annualized_volatility, \
    calculate_sharpe_ratio, compare_with_buy_hold


class Backtester:
    """for backtesting trading strategies"""

    def __init__(self,  tickers: list[str], initial_capital: float=10000.0, commission_rate: float=0.001):
        self.initial_capital = initial_capital
        self.commission_rate = commission_rate
        self.assets_data:Dict = {}
        self.portfolio_history:Dict = {}
        self.daily_portfolio_value: list[float] = []
        self.buy_hold_portfolio_value: list[float] = []
        self.tickers = tickers

    def trade_executor(self, asset: str, signal: int, price: float):

        if signal > 0 and self.assets_data[asset]["cash"] > 0:
            trade_value = self.assets_data[asset]["cash"]
            commission = self.commission_rate * trade_value
            shares_to_buy = (trade_value-commission)/price
            self.assets_data[asset]["cash"] -= trade_value
            self.assets_data[asset]["positions"] += shares_to_buy

        if signal <0 and self.assets_data[asset]["positions"] > 0:
            trade_value = self.assets_data[asset]["positions"] * price
            commission = self.commission_rate * trade_value
            self.assets_data[asset]["positions"] = 0
            self.assets_data[asset]["cash"] += trade_value - commission


    def update_portfolio(self, asset: str, price: float):
        self.assets_data[asset]["position_value"] = price * self.assets_data[asset]["positions"]
        self.assets_data[asset]["total_value"] = self.assets_data[asset]["position_value"] + self.assets_data[asset]["cash"]
        self.portfolio_history[asset].append(self.assets_data[asset]["total_value"])

    def buy_and_hold(self, data: pd.DataFrame):
        allocation = self.initial_capital / len(self.tickers)
        allocation-=self.commission_rate*allocation
        shares_bought = allocation / data["Close"].iloc[0]
        portfolio_values = data["Close"].mul(shares_bought, axis=1)
        buy_and_hold_curve = portfolio_values.sum(axis=1)
        return buy_and_hold_curve

    def backtest(self, data: pd.DataFrame, tickers: list[str]):
        """Backtest the strategy"""
        for ticker in tickers:
            self.assets_data[ticker] = {
                "cash": self.initial_capital / len(tickers),
                "positions": 0,
                "position_value": 0,
                "total_value": 0
            }
            self.portfolio_history[ticker] = []
            asset_data = data.xs(ticker, level="Ticker", axis=1)
            asset_data["Position"] = asset_data["Signal"].shift(1).fillna(0)
            for date, row in asset_data.iterrows():
                self.trade_executor(ticker, row['Position'], row['Close'])
                self.update_portfolio(ticker, row['Close'])
                if len(self.daily_portfolio_value) < len(asset_data):
                    self.daily_portfolio_value.append(self.assets_data[ticker]["total_value"])
                else:
                    self.daily_portfolio_value[len(self.portfolio_history[ticker])-1] += self.assets_data[ticker]["total_value"]



    def calculate_performance(self, data: pd.DataFrame):

        portfolio_values = pd.Series(self.daily_portfolio_value)
        daily_returns = portfolio_values.pct_change().dropna()

        total_return = calculate_total_return(portfolio_values.iloc[-1], self.initial_capital)
        annualized_return = calculate_annualized_return(total_return, len(portfolio_values))
        annualized_volatility = calculate_annualized_volatility(daily_returns)
        sharpe_ratio = calculate_sharpe_ratio(annualized_return, annualized_volatility)

        print(f"Final Value: {portfolio_values.iloc[-1]:.2f}")
        print(f"Total Return: {total_return * 100:.2f}%")
        print(f"Annualized Return: {annualized_return * 100:.2f}%")
        print(f"Annualized Volatility: {annualized_volatility * 100:.2f}%")
        print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

        print(self.buy_and_hold(data).iloc[-1])
        buy_hold_returns = self.buy_and_hold(data).pct_change().dropna()
        daily_returns.index = buy_hold_returns.index
        portfolio_values.index = data.index

        self.plot_performance(portfolio_values, daily_returns)
        compare_with_buy_hold(buy_hold_returns, daily_returns)


    def plot_performance(self, portfolio_values, daily_returns):
        """Plot the performance of the trading strategy."""
        plt.figure(figsize=(10, 6))

        plt.subplot(2, 1, 1)
        plt.plot(portfolio_values, label="Portfolio Value", color="blue")
        plt.title("Portfolio Value Over Time")
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(daily_returns, label="Daily Returns", color="red")
        plt.title("Daily Returns Over Time")
        plt.legend()

        plt.tight_layout()
        plt.show()
