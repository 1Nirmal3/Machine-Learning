from autots import AutoTS
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import regression
sns.set()
plt.style.use('seaborn-whitegrid')

import streamlit as st
st.title("Future Price Prediction Model")
df = st.text_input("Let's Predict the Future Prices")

df=df.lower()
data=yf.Ticker(df)
historical_data=pd.DataFrame(data.history(period="max"))
historical_data.dropna()
model = AutoTS(forecast_length=10, frequency='infer', ensemble='simple', drop_data_older_than_periods=200,model_list="fast_parallel",
               transformer_list="superfast")
model = model.fit(data, date_col='Date', value_col='Close', id_col=None)
prediction = model.predict()
forecast = prediction.forecast
st.write(forecast)