import yfinance as np
import streamlit as st

st.write("""
# SIMPLE STOCK PRICE APP

Shown are the **stock closing price** and **volume** of Google!""" )

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symol
 tickerSymbol ='GOOGL'
 # GET DATA ON THIS ticker
 tickerData = yf.Ticker(tickerSymbol)
 # get the historical prices for this tickerData
 tickerDf = tickerData.history(period='1d', start='2010-5-31', ends='2020-5-31')

 #Open High Low Close Volume Dividends   Stock Splits

 st.line_chart(tickerDf.Close)
 st.line_chart(tickerDf.Volume)
