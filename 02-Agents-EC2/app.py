import re
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DDGS
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

def search_web(query: str) -> str:
    """Searches DuckDuckGo for the given query and returns results."""
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=5)]
        return str(results)

########## Agentes de IA ##########
# Agentes de IA 
web_search_agent = Agent(name="Web Search Agent",
                              role="To search the web",
                              model=Groq(id="llama-3.3-70b-versatile"),
                              tools=[search_web],
                              instructions=["Always includes the sources"],
                              show_tool_calls=True, markdown=True)

financial_agent = Agent(name="Financial Agent",
                              model=Groq(id="llama-3.3-70b-versatile"),
                              tools=[YFinanceTools(stock_price=True,
                                                   analyst_recommendations=True,
                                                   stock_fundamentals=True,
                                                   company_news=True)],
                              instructions=["Use tables to show the data"],
                              show_tool_calls=True, markdown=True)

multi_ai_agent = Agent(team=[web_search_agent, financial_agent],
                       model=Groq(id="llama-3.3-70b-versatile"),
                       instructions=["Always include sources", "Use tables to show the data"],
                       show_tool_calls=True, markdown=True)

########## App Web ##########
st.set_page_config(page_title="Real-Time Day Trading Analytics", page_icon=":100:", layout="wide")

# Sidebar
st.sidebar.title("Instructions")
st.sidebar.markdown("""
### How to use the App:

- Enter the ticker symbol of the desired stock in the central field.
- Click the **Analyze** button to obtain real-time analysis with AI-generated visualizations and insights.

### Examples of valid tickers:
- MSFT (Microsoft)
- TSLA (Tesla)
- AMZN (Amazon)
- GOOG (Alphabet)

More tickers can be found here: https://stockanalysis.com/list/nasdaq-stocks/

### Purpose of the App:
This application performs advanced real-time Nasdaq stock price analysis using AI Agents with the DeepSeek model through Groq and AWS infrastructure to support day trading strategies for monetization. A complete example app for those who want to start in Data and AI Consulting.
""")

# st.title(":100: Real-Time Day Trading Analytics")
st.header("Real-time Day Trading Analytics with AI Agents")

# User input
ticker = st.text_input("Enter the ticker code").upper()


if st.button("Send"):

    if ticker:

        with st.spinner("Retrieving real-time data. Please wait..."):
            
            hist = extract_data(ticker)
            
            st.subheader("AI-Generated Analysis")
            
            # Run the AI ​​Agents team
            ai_response = multi_ai_agent.run(f"Summarize the analyst recomendation and share the last news about {ticker}")

            # Removing lines which start with "Running:"
            # Removing the block "Running:" and lines "transfer_task_to_finance_ai_agent"
            clean_response = re.sub(r"(Running:[\s\S]*?\n\n)|(^transfer_task_to_finance_ai_agent.*\n?)","", ai_response.content, flags=re.MULTILINE).strip()

            st.markdown(clean_response)

            # Render the plots
            st.subheader("Data Visualization")
            plot_stock_price(hist, ticker)
            plot_candlestick(hist, ticker)
            plot_moving_average(hist, ticker)
            plot_volume(hist, ticker)
    else:
        st.error("Invalid ticker. Enter a valid ticker.")

