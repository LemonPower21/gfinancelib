# Stock & Financial Data Analysis Script

This Python script allows you to fetch, analyze, and display stock-related information for various tickers. The script leverages the `yfinance` library to retrieve stock data, calculates technical indicators like EMA (Exponential Moving Average) and RSI (Relative Strength Index), and provides detailed market information such as bid/ask prices, volume, market cap, and more.
## Created by: Francesco Vito Giotta (LemonPower21)

This library was created by Francesco Vito Giotta to provide a set of tools for financial analysis using Python. It leverages the `yfinance` and `ta` libraries for retrieving stock data, calculating technical indicators, and sending email notifications.
## Features

- **Stock Data Retrieval**: Fetches live stock data (bid, ask, volume, etc.) for a given ticker symbol.
- **Technical Indicators**: Computes key technical indicators like **RSI**, **EMA**, and **ATH** (All-Time High).
- **Market Information**: Provides details such as market cap, shares outstanding, exchange, currency, etc.
- **Real-time Alerts**: Optionally sends alerts or logs when certain conditions are met.
- **Email Notifications**: Sends email alerts with detailed data logs attached.
- **Customizable Output**: Displays stock information in a user-friendly formatted table.

## Requirements

- Python 3.x
- `yfinance` library
- `ta` (technical analysis library)
- `smtplib` for sending emails
- `colorama` for colored output in the terminal

You can install the required libraries by running the following:

```bash
pip install yfinance ta colorama
```

## Functions

### `bid(ticker)`
- **Purpose**: Retrieves the current bid price for the specified stock ticker.
- **Returns**: The bid price (float) or `0` if unavailable.

### `ask(ticker)`
- **Purpose**: Retrieves the current ask price for the specified stock ticker.
- **Returns**: The ask price (float) or `0` if unavailable.

### `start()`
- **Purpose**: Records the start time for calculating the elapsed time.

### `stop(start)`
- **Purpose**: Calculates and returns the elapsed time since the provided `start` time.
- **Returns**: Elapsed time in years, months, days, hours, minutes, and seconds.

### `log(text)`
- **Purpose**: Logs events to a file (`log.txt`).
- **Returns**: None.

### `last(ticker)`
- **Purpose**: Retrieves the last closing price for the specified ticker.
- **Returns**: The last closing price (float) or `None` if unavailable.

### `rsi(ticker, periods, chart, timeframe)`
- **Purpose**: Calculates the RSI (Relative Strength Index) for the specified ticker.
- **Returns**: The RSI value (float) or `None` if unavailable.

### `ema(ticker, periods, chart, timeframe)`
- **Purpose**: Calculates the Exponential Moving Average (EMA) for the specified ticker.
- **Returns**: The EMA value (float) or `None` if unavailable.

### `clean()`
- **Purpose**: Clears the terminal screen (cross-platform support).

### `email(server, port, user, password, recipient, subject, body)`
- **Purpose**: Sends an email with the log file attached.
- **Returns**: None.

### `ychart(ticker)`
- **Purpose**: Opens the Yahoo Finance chart for the specified ticker in a browser.
- **Returns**: None.

### `ynews()`
- **Purpose**: Opens the Yahoo Finance news page in a browser.
- **Returns**: None.

### `change(pair)`
- **Purpose**: Retrieves the exchange rate for a given currency pair against EUR.
- **Returns**: Exchange rate (float) or `None` if unavailable.

### `ath(ticker)`
- **Purpose**: Retrieves the All-Time High (ATH) for the specified ticker.
- **Returns**: ATH value (float) or `None` if unavailable.

### `currency(ticker)`
- **Purpose**: Retrieves the currency used by the stock ticker.
- **Returns**: Currency symbol (e.g., USD, EUR) or `None` if unavailable.

### `exchange(ticker)`
- **Purpose**: Retrieves the exchange name for the specified ticker.
- **Returns**: Exchange name (string) or `None` if unavailable.

### `volume(ticker)`
- **Purpose**: Retrieves the real-time market volume for the specified ticker.
- **Returns**: Volume (integer) or `None` if unavailable.

### `marketcap(ticker)`
- **Purpose**: Retrieves the market capitalization for the specified ticker.
- **Returns**: Market cap (float) or `None` if unavailable.

### `shares(ticker)`
- **Purpose**: Retrieves the shares outstanding for the specified ticker.
- **Returns**: Shares outstanding (integer) or `None` if unavailable.

### `invested(qty, buyprice)`
- **Purpose**: Calculates the total amount invested based on the quantity and buy price.
- **Returns**: Investment amount (float) or `None` if unavailable.

### `roi(buyprice, lastprice)`
- **Purpose**: Calculates the Return on Investment (ROI) percentage based on the buy price and last price.
- **Returns**: ROI percentage (float) or `None` if unavailable.

### `pandl(roiperc, invested)`
- **Purpose**: Calculates the profit or loss based on the ROI percentage and investment.
- **Returns**: Profit or loss (float) or `None` if unavailable.

### `initprint()`
- **Purpose**: Initializes the table header for formatted output in the terminal.
- **Returns**: None.

### `printall(...)`
- **Purpose**: Prints detailed stock information including price, indicators, market data, and elapsed time in a formatted table.
- **Returns**: None.

## Usage Example

Here's how to use the script:

1. **Get stock data**:  
   Call the functions for your desired ticker, e.g., `bid('AAPL')` or `rsi('AAPL', 14, '1d', '5m')`.

2. **Track a stock's performance**:  
   Use `printall(...)` to display the stock's information in a table format.

3. **Email log**:  
   Use the `email(...)` function to send an email with the logs attached.

4. **View charts and news**:  
   Use `ychart()` and `ynews()` to view the latest stock charts and news.

## Example Output

```
Ticker      Exchange   Currency   Change    Quantity   Invested   Buy     Last     TP(%)    P&L(%)  P&L(€)  EMA      RSI     ATH      Bid      Ask      Spread   Shares   Volume   MarketCap      Elapsed time
AAPL        NASDAQ     USD        0.0056    100        15000.00   150.00  153.20   2.00     2.14    320.00  150.10   45.32   157.89   152.50   153.50   1.00     1000     50000    2.5B    1Y, 2M, 3d, 4h, 5m, 6.00s
```

## Conclusion

This script is a powerful tool for analyzing and tracking stock market data in real-time. With easy-to-use functions for retrieving financial data, computing technical indicators, and generating reports, it's a great resource for traders, analysts, and developers alike.

---
