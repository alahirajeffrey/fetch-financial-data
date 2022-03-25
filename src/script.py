import yfinance as yf

# get user inputs
TICKER = input("Enter ticker : ")
START = input("Enter start date : ")
END = input("Enter end date : ")

# function to fetch data


def fetch_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data


if __name__ == "__main__":
    fetch_data(TICKER, START, END)
