import yfinance as yf
import pandas as pd
from datetime import datetime
from ticker import tickers
def fetch_stock_data(tickers, start_date, end_date):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        history = stock.history(start=start_date, end=end_date)
        data[ticker] = history['Close']
    return data

def calculate_returns(stock_data):
    returns = {}
    for ticker, prices in stock_data.items():
        if len(prices) < 2:
            continue  # Skip stocks with insufficient data
        start_price = prices.iloc[0]
        end_price = prices.iloc[-1]
        returns[ticker] = (end_price - start_price) / start_price * 100
    return returns

def get_top_stocks(returns, top_n=20):
    sorted_returns = sorted(returns.items(), key=lambda x: x[1], reverse=True)
    return sorted_returns[:top_n]

def main():
    # Get user input
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    number_of_tocks = int(input("Enter the number of stocks yow want to see: "))

    
    # Fetch stock data
    stock_data = fetch_stock_data(tickers, start_date, end_date)
    
    print(f"Fetching data for {len(tickers)} stocks from {start_date} to {end_date}...")
    # Calculate returns
    returns = calculate_returns(stock_data)
    
    # Get top performer stocke
    top_stocks = get_top_stocks(returns, number_of_tocks)
    
    # Display results
    print(f"\nTop {number_of_tocks} Stocks by Return:")
    for ticker, return_percent in top_stocks:
        print(f"{ticker}: {return_percent:.2f}%")

if __name__ == "__main__":
    main()
