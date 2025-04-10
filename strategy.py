from typing import Callable, Dict

import pandas as pd


IndicatorFunction = Callable[[pd.DataFrame], pd.Series]
SignalLogicFunction = Callable[[pd.Series], int]

class Strategy:

    def __init__(self, tickers:list[str], indicators: Dict[str, IndicatorFunction], signal_logic: SignalLogicFunction) -> None:
        self.indicators = indicators
        self.signal_logic = signal_logic
        self.tickers = tickers

    def apply_strategy(self, df: pd.DataFrame) -> pd.DataFrame:

        for ticker in self.tickers:
            data = df.xs(ticker, level="Ticker", axis=1)
            for name, indicator in self.indicators.items():
                df[(name, ticker)] = indicator(data)
            data = df.xs(ticker, level="Ticker", axis=1)
            df[("Signal", ticker)] = data.apply(lambda x: self.signal_logic(x), axis=1)
            df[("Position", ticker)] = df[("Signal", ticker)].replace(to_replace=0, method='ffill')
        return df

    def generate_signals(self, df: pd.DataFrame) -> pd.DataFrame:
        return self.apply_strategy(df)