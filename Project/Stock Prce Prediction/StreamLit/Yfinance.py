import yfinance as yf
import pandas as pd
data_=input("Enter Code:")
data=yf.Ticker(data_)
print(pd.DataFrame(data.history(period="max")))
