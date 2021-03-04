import streamlit as st 
import pandas as pd 
import yfinance as yf 

st.write("""
# A simple stock application

Shown are the stock closing price and volume of Google!
"""
)

# to define the ticker symbol
tickerSymbol = 'GOOGL'

# To get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#to get historical prices for this ticker
tickerDf = tickerData.history(period = '1d', start = '2021-01-01', end = '2021-03-03')

# Open   High   Low   Close  Volume   Dividends  Stock Splits


st.write("""
Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
Volume
""")
st.line_chart(tickerDf.Volume)
