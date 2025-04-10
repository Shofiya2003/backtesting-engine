import yfinance as yf
import pandas as pd
class DataHandler:
    """Data Handler class loads the data"""

    def __init__(self, tickers: list[str], start_date: str, end_date: str):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.data = pd.DataFrame()

    def load_data(self)->pd.DataFrame:
        self.data = yf.download(tickers=self.tickers, start=self.start_date, end=self.end_date)
        return self.data

