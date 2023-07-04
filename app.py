# Сделайте своё приложение на русском языке на платформе Streamlit с данными о котировках компании 
# Apple c помощью библиотеки yfinance

import yfinance as yf
import streamlit as st

st.write("""
# Простое приложение для отслеживания акций

На графике редставлены **цена закрытия** и ***объём*** торгов по акциям Apple!

""")

#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-7-3', end=None)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Цена закрытия
""")
st.line_chart(tickerDf.Close)
st.write("""
## Объём торгов
""")
st.line_chart(tickerDf.Volume)
st.write("""
## Дивиденды
""")
st.line_chart(tickerDf.Dividends)