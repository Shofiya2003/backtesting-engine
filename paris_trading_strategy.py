from strategy import Strategy

# Correlation between the Close of stock in consideration and stock B
# print(data[["Close", "Close_B"]].corr())

# Close_B is the price of the correlated stock
indicators = {
    "price_ratio": lambda df: df["Close"] / df["Close_B"],
    "z_score": lambda df: (df["price_ratio"] - df["price_ratio"].rolling(20).mean()) / df["price_ratio"].rolling(20).std()
}

signal_logic = lambda row: -1 if row["z_score"] > 1 else (1 if row["z_score"] < -1 else 0)

paris_trading_strategy = Strategy(
    [],
    indicators,
    signal_logic,
)