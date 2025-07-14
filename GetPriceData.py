import yfinance as yf
import pandas as pd
import numpy as np


class GetPriceData:
    
    def get_PriceData(tickers, startdate, enddate) -> pd.DataFrame:
        """Gets the data from yfinance for the ticker and dates

        Args:
            tickers (_type_): _description_
            startdate (_type_): _description_
            enddate (_type_): _description_

        Returns:
            pd.DataFrame: _description_
        """
        
        
        data = yf.download(tickers= tickers, start= startdate, end= enddate, auto_adjust= False)["Adj Close"]
        return data.dropna()
    
    
    def get_returns(price_df: pd. DataFrame, method: str) -> pd.DataFrame:
        """
        Calculates the returns for the Adjusted Closing Prices
        simple: Calculates the pct_change
        log: log returns

        Args:
            price_df (pd.DataFrame): _description_
            method (str): _description_

        Returns:
            pd.DataFrame: _description_
        """
        
        if method == "simple":
            price_df = price_df.pct_change().dropna()
        elif method == "log":
            price_df = np.log(price_df / price_df.shift(1)).dropna()
            
        return price_df
        