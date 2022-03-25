import yfinance as yf
import pandas as pd

# get user inputs
TICKER = input("Enter ticker : ")
START = input("Enter start date : ")
END = input("Enter end date : ")

# function to fetch data


def fetch_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)

    # save to csv file
    data.to_csv(f'{ticker}.csv', encoding='utf-8')
    print("Data stored in csv file!!")


if __name__ == "__main__":
    fetch_data(TICKER, START, END)
