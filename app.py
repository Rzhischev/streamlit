# Сделайте своё приложение на русском языке на платформе Streamlit с данными о котировках компании 
# Apple c помощью библиотеки yfinance

import yfinance as yf
import streamlit as st

st.write("""
# Простое приложение для отслеживания акций

На графике представлены **цена закрытия**, ***объём*** торгов и другие ключевые метрики по акциям Apple!

""")

#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-7-3', end=None)
#				Stock Splits

st.write("""
## Минимальная цена
""")
st.line_chart(tickerDf.Low)
st.write("""
## Максимальная цена
""")
st.line_chart(tickerDf.High)
st.write("""
## Цена открытия
""")
st.line_chart(tickerDf.Open)
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
