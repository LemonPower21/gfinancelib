# Financial Data Analysis Library

## Overview
This library provides a set of functions for financial analysis using the `yfinance` and `ta` libraries. It includes functionalities for retrieving stock prices, calculating financial indicators, sending notifications, and more.

## Functions

### `bid(ticker)`
Fetches the bid price of the specified ticker.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
- **Returns:**
  - `float`: The bid price, or `None` if an error occurs.

### `ask(ticker)`
Fetches the ask price of the specified ticker.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
- **Returns:**
  - `float`: The ask price, or `None` if an error occurs.

### `start()`
Starts a timer and returns the current time.

- **Returns:**
  - `float`: The start time in seconds.

### `stop(start)`
Stops the timer and returns the elapsed time in years, months, days, hours, minutes, and seconds.

- **Parameters:**
  - `start` (float): The start time returned from the `start()` function.
- **Returns:**
  - `tuple`: Elapsed time in years, months, days, hours, minutes, and seconds.

### `log(text)`
Logs an update with a timestamp to a `log.txt` file.

- **Parameters:**
  - `text` (str): The text to log.
- **Returns:**
  - None

### `last(ticker)`
Fetches the last closing price of the specified ticker.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
- **Returns:**
  - `float`: The last closing price, or `None` if an error occurs.

### `rsi(ticker, periods, chart, timeframe)`
Calculates the Relative Strength Index (RSI) for the specified ticker.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
  - `periods` (int): The number of periods to use for the RSI calculation.
  - `chart` (str): The period of chart data to use.
  - `timeframe` (str): The interval of the chart data.
- **Returns:**
  - `float`: The RSI value, or `None` if an error occurs.

### `ema(ticker, periods, chart, timeframe)`
Calculates the Exponential Moving Average (EMA) for the specified ticker.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
  - `periods` (int): The number of periods to use for the EMA calculation.
  - `chart` (str): The period of chart data to use.
  - `timeframe` (str): The interval of the chart data.
- **Returns:**
  - `float`: The EMA value, or `None` if an error occurs.

### `clean()`
Clears the console screen.

- **Returns:** None

### `email(server, port, user, password, recipient, subject, body)`
Sends an email with the log file attached to a recipient using an SMTP server.

- **Parameters:**
  - `server` (str): The SMTP server address.
  - `port` (int): The SMTP server port.
  - `user` (str): The sender's email address.
  - `password` (str): The sender's email password.
  - `recipient` (str): The recipient's email address.
  - `subject` (str): The subject of the email.
  - `body` (str): The body of the email.
- **Returns:**
  - None

### `ychart(ticker)`
Opens the Yahoo Finance chart for the specified ticker in a web browser.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.

### `ynews()`
Opens the Yahoo Finance news page in a web browser.

### `change(pair)`
Fetches the exchange rate for the specified currency pair.

- **Parameters:**
  - `pair` (str): The currency pair (e.g., "USDJPY").
- **Returns:**
  - `float`: The exchange rate, or `None` if an error occurs.

### `ath(ticker)`
Fetches the all-time high (ATH) for the specified ticker.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
- **Returns:**
  - `float`: The all-time high value, or `None` if an error occurs.

### `currency(ticker)`
Fetches the currency in which the specified ticker is traded.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
- **Returns:**
  - `str`: The currency, or `None` if an error occurs.

### `exchange(ticker)`
Fetches the exchange where the specified ticker is traded.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
- **Returns:**
  - `str`: The exchange, or `None` if an error occurs.

### `volume(ticker)`
Fetches the trading volume of the specified ticker.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
- **Returns:**
  - `int`: The trading volume, or `None` if an error occurs.

### `marketcap(ticker)`
Fetches the market capitalization of the specified ticker.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
- **Returns:**
  - `float`: The market capitalization, or `None` if an error occurs.

### `shares(ticker)`
Fetches the number of shares outstanding for the specified ticker.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
- **Returns:**
  - `int`: The number of shares outstanding, or `None` if an error occurs.

## Usage Examples

Here are a few examples to help you get started:

```python
# Get the bid price of AAPL
print(bid("AAPL"))

# Get the ask price of AAPL
print(ask("AAPL"))

# Start a timer and stop after 2 seconds
start_time = start()
time.sleep(2)
elapsed_time = stop(start_time)
print(f"Elapsed time: {elapsed_time} years, months, days, hours, minutes, seconds")

# Log an update
log("Stock market update: AAPL is trending up.")

# Get the last closing price of AAPL
print(last("AAPL"))

# Calculate the RSI for AAPL
print(rsi("AAPL", 14, "2y", "1h"))

# Calculate the EMA for AAPL
print(ema("AAPL", 200, "2y", "1h"))

# Send an email with the log file
email("smtp.gmail.com", 587, "your_email@gmail.com", "your_email_password", "recipient_email@example.com", "Stock Data Update", "Please find the stock data update attached.")

# Open the Yahoo Finance chart for AAPL
ychart("AAPL")

# Open Yahoo Finance news page
ynews()

# Get the exchange rate for USD to EUR
print(change("USD"))

# Get the all-time high for AAPL
print(ath("AAPL"))

# Get the currency in which AAPL is traded
print(currency("AAPL"))

# Get the exchange where AAPL is traded
print(exchange("AAPL"))

# Get the trading volume of AAPL
print(volume("AAPL"))

# Get the market cap of AAPL
print(marketcap("AAPL"))

# Get the number of shares outstanding for AAPL
print(shares("AAPL"))

# Clear the console screen
clean()
## Additional Information

- **Dependencies**: This library requires the following Python libraries:
  - `yfinance`
  - `ta`
  - `time`
  - `os`
  - `platform`
  - `smtplib`
  - `webbrowser`
  - `datetime`
  - and other related libraries.

**Installation**: You can install the necessary modules using:

  ```bash
  pip install yfinance ta


- Created by Francesco Vito Giotta (LemonPower21)
- LinkedIn: https://www.linkedin.com/in/francesco-vito-giotta-969938314/
- GitHub: https://github.com/LemonPower21/gfinancelib
