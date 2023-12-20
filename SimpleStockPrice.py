import yfinance as yf #used for analysing financial data
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Apple!

"""
	)

tickersymbol='AAPL'

tickerdata = yf.Ticker(tickersymbol) #Ticker used for interacting with Yahoo Finance API

tickerDf = tickerdata.history(period='1d', start='2022-5-31', end='2023-5-31')

#st.write(tickerDf.columns)

st.write("""
### Closing Price
""")
st.line_chart(tickerDf['Close'])

st.write("""
### Volume
""")
st.line_chart(tickerDf['Volume'])
