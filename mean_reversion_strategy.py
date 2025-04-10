from strategy import Strategy

indicators = {
    "sma_20": lambda df: df["Close"].rolling(window=20).mean()
}

signal_logic = lambda row: 1 if row["sma_20"] > row["Close"] else -1

mean_reversion_strategy = Strategy([], indicators, signal_logic)