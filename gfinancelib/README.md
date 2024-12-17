# Library Documentation

## Overview
This library provides a set of functions for financial analysis using the `yfinance` and `ta` libraries. It includes functionalities for retrieving stock prices, calculating financial indicators, and sending notifications.

## Functions

### `last(ticker)`
Fetches the last closing price of the specified ticker.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
- **Returns:**
  - `float`: The last closing price, or `None` if an error occurs.

### `roi(ticker, buy)`
Calculates the Return on Investment (ROI) for the specified ticker and buy price.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
  - `buy` (float): The buy price of the stock.
- **Returns:**
  - `float`: The ROI in percentage, or `None` if an error occurs.

### `rsi(ticker, periods, chart_data, timeframe)`
Calculates the Relative Strength Index (RSI) for the specified ticker.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
  - `periods` (int): The number of periods to use for the RSI calculation.
  - `chart_data` (str): The period of chart data to use.
  - `timeframe` (str): The interval of the chart data.
- **Returns:**
  - `float`: The RSI value, or `None` if an error occurs.

### `ema(ticker, periods, chart_data, timeframe)`
Calculates the Exponential Moving Average (EMA) for the specified ticker.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
  - `periods` (int): The number of periods to use for the EMA calculation.
  - `chart_data` (str): The period of chart data to use.
  - `timeframe` (str): The interval of the chart data.
- **Returns:**
  - `float`: The EMA value, or `None` if an error occurs.

### `profit(ticker, buy, qty)`
Calculates the profit for the specified ticker, buy price, and quantity.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
  - `buy` (float): The buy price of the stock.
  - `qty` (float): The quantity of the stock.
- **Returns:**
  - `float`: The profit, or `None` if an error occurs.

### `invested(buy, qty)`
Calculates the invested amount for the specified buy price and quantity.

- **Parameters:**
  - `buy` (float): The buy price of the stock.
  - `qty` (float): The quantity of the stock.
- **Returns:**
  - `float`: The invested amount, or `None` if an error occurs.

### `telegram(token, id, message)`
Sends a message via Telegram.

- **Parameters:**
  - `token` (str): The Telegram bot token.
  - `id` (str): The chat ID.
  - `message` (str): The message to send.
- **Returns:**
  - `dict`: The response from the Telegram API, or `None` if an error occurs.

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

### `get_currency(ticker)`
Fetches the currency in which the specified ticker is traded.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
- **Returns:**
  - `str`: The currency, or `None` if an error occurs.

### `get_exchange(ticker)`
Fetches the exchange where the specified ticker is traded.

- **Parameters:**
  - `ticker` (str): The ticker symbol of the stock.
- **Returns:**
  - `str`: The exchange, or `None` if an error occurs.

### `clean()`
Clears the console screen.

- **Parameters:** None
- **Returns:** None

## Usage Examples

Here are a few examples to help you get started:

```python
# Get the last closing price of AAPL
print(last("AAPL"))

# Calculate the ROI for AAPL with a buy price of 120
print(roi("AAPL", 120))

# Calculate the RSI for AAPL
print(rsi("AAPL", 14, "2y", "1h"))

# Calculate the EMA for AAPL
print(ema("AAPL", 200, "2y", "1h"))

# Calculate the profit for AAPL
print(profit("AAPL", 120, 10))

# Calculate the invested amount
print(invested(120, 10))

# Send a Telegram message
telegram("<your_token>", "<your_chat_id>", "Hello from the bot!")

# Open Yahoo Finance chart for AAPL
ychart("AAPL")

# Open Yahoo Finance news page
ynews()

# Get the exchange rate for USD to EUR
print(change("USD"))

# Get the all-time high for AAPL
print(ath("AAPL"))

# Get the currency in which AAPL is traded
print(get_currency("AAPL"))

# Get the exchange where AAPL is traded
print(get_exchange("AAPL"))

# Clear the console screen
clean()
```

## Additional Information

- **Dependencies**: This library requires the `yfinance`, `requests`, `ta`, `pandas`, and `webbrowser` modules.
- **Installation**: You can install the necessary modules using:
  ```bash
  pip install yfinance requests ta pandas
  ```

- Created by Francesco Vito Giotta (LemonPower21)
- LinkedIn: https://www.linkedin.com/in/francesco-vito-giotta-969938314/
- GitHub: https://github.com/LemonPower21/gfinancelib
