# Backtesting Engine
Backtesting Engine is a project that allows you to design, test and evaluate trading strategies using historical market data. The tool enables quantitative analysts to assess the effectiveness of their strategies before applying them in live markets. 

## 🚀 Features

📈 Custom Strategies: Implement strategies like Mean Reversion, Moving Average Crossover, and Pairs Trading.

🧠 Signal-Based Execution: Uses generated buy/sell signals to simulate trades over time.

💰 Capital Allocation: Handles initial capital and trade execution per signal.

📊 Performance Metrics: Outputs key metrics like total return, Sharpe ratio, and annualized return.

📉 Buy & Hold Benchmark: Compares active strategies against passive investing.

## 🧩 How It Works

**Input:**

Initial capital (e.g., $10,000)

List of stocks (e.g., ['AAPL', 'GOOG'])

Date range for backtesting (e.g., 2020–2024)

**Signal Generation:**

A trading strategy (e.g., mean reversion) calculates when to buy or sell each stock using historical price data.

**Trade Execution:**

Based on signals, trades are simulated using the given capital. The engine tracks how many shares are bought/sold and calculates transaction costs if needed.

**Portfolio Valuation:**

Computes the portfolio value over time based on executed trades and market prices.

**Comparison with Buy & Hold:**

Evaluates how the custom strategy performs compared to simply buying and holding the same stocks over the same period.

## Example

For a comprehensive example, refer to the main.py script, which demonstrates the entire workflow from data acquisition to performance evaluation.

```
# Prepare the data
tickers = ["GOOG"]
data = DataHandler(tickers, "2021-01-01", "2024-12-31").load_data()
mean_reversion_strategy.tickers = tickers

# Create a Strategy
mean_reversion_strategy.apply_strategy(data)

# Backtest
backtester = Backtester(tickers=tickers)
backtester.backtest(data, tickers)
backtester.calculate_performance(data)
```
![image](https://github.com/user-attachments/assets/cdc3092a-76e9-472c-bf06-62acf63d0b61)


![image](https://github.com/user-attachments/assets/277e8880-b8b9-4694-831e-b518c68a084c)

