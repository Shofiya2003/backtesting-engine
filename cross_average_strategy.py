from strategy import Strategy

cross_average_strategy = Strategy(
    [],
    indicators={
        "sma_20": lambda row: row["Close"].rolling(window=20).mean(),
        "sma_60": lambda row: row["Close"].rolling(window=60).mean(),
    },
    signal_logic=lambda row: 1 if row["sma_20"] > row["sma_60"] else -1,
)