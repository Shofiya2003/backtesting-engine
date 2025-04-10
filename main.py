from backtester import Backtester
from dataHandler import DataHandler
from paris_trading_strategy import paris_trading_strategy
from strategy import Strategy

# Prepare the data
tickers = ["NVDA"]
data = DataHandler(tickers, "2021-01-01", "2024-12-31").load_data()
data_rotu = DataHandler(["AMD"], "2023-01-01", "2023-12-31").load_data()
data[("Close_B", "NVDA")] = data_rotu.xs(key="AMD", level="Ticker", axis=1)["Close"]
paris_trading_strategy.tickers = tickers

# Create a Strategy
paris_trading_strategy.apply_strategy()

# Backtest
backtester = Backtester()
backtester.backtest(data, tickers)
backtester.calculate_performance()