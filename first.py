import yfinance as yf
import streamlit as st
import pandas as pd
import datetime

today = datetime.datetime.now()

d_start = st.date_input(
    "Select start date of data",
    today,
    format="MM.DD.YYYY",
)

st.write("# Simple stock price of GOOGLE")
tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period = '1d', start= d_start, end= today)

#st.write(tickerDF)

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)