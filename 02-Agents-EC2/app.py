import re
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv


load_dotenv()


########## Analytics ##########
@st.cache_data
def extract_data(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)    
    hist.reset_index(inplace=True)
    return hist


def plot_stock_price(hist, ticker):
    fig = px.line(hist, x="Date", y="Close", title=f"{ticker} Stock Prices (Last 6 Months)", markers=True)    
    st.plotly_chart(fig)

def plot_candlestick(hist, ticker):
    fig = go.Figure(data=[go.Candlestick(x=hist['Date'], open=hist['Open'], high=hist['High'], low=hist['Low'], close=hist['Close'])])
    fig.update_layout(title=f"{ticker} Candlestick Chart (Last 6 Months)")
    st.plotly_chart(fig)

def plot_moving_average(hist, ticker):
    # Calculates the 20-period Simple Moving Average (SMA) and adds it to the DataFrame.
    hist['SMA_20'] = hist['Close'].rolling(window=20).mean()
    # Calculates the 20-period Exponential Moving Average (EMA) and adds it to the DataFrame.
    hist['EMA_20'] = hist['Close'].ewm(span=20, adjust=False).mean()
    
    fig = px.line(hist, x='Date', y=['Close', 'SMA_20', 'EMA_20'], title=f"{ticker} Moving Average (Last 6 Months)", labels={'value': 'Price (USD)', 'Date': 'Date'})
    st.plotly_chart(fig)

def plot_volume(hist, ticker):
    fig = px.bar(hist, x='Date', y='Volume', title=f"{ticker} Trading Volume (Last 6 Months)")    
    st.plotly_chart(fig)

########## Agentes de IA ##########



########## App Web ##########