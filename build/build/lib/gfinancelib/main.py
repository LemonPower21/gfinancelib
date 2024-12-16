
def last(ticker):
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    try:
        stock = yf.Ticker(ticker)
        last = stock.history(period="1d", interval="1m").iloc[-1]['Close']
        return last
    except Exception as e:
        print(f"Error fetching last price for {ticker}: {e}")
        return None

def roi(ticker, buy):
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    try:
        stock = yf.Ticker(ticker)
        last = float(stock.history(period="1d", interval="1m").iloc[-1]['Close'])
        r = float((((last - buy) / buy) * 100))
        return r
    except Exception as e:
        print(f"Error calculating ROI for {ticker}: {e}")
        return None

def rsi(ticker, periods, chart_data, timeframe):
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=chart_data, interval=timeframe)
        data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=periods).rsi()
        return float(data['RSI'].iloc[-1])
    except Exception as e:
        print(f"Error calculating RSI for {ticker}: {e}")
        return None

def ema(ticker, periods, chart_data, timeframe):
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=chart_data, interval=timeframe)
        ema = data['Close'].ewm(span=periods, adjust=False).mean()
        return float(ema.iloc[-1])
    except Exception as e:
        print(f"Error calculating EMA for {ticker}: {e}")
        return None

def profit(ticker, buy, qty):
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    try:
        stock = yf.Ticker(ticker)
        last = stock.history(period="1d", interval="1m").iloc[-1]['Close']
        return float(((((last - buy) / buy) * 100) * (qty * buy)))
    except Exception as e:
        print(f"Error calculating profit for {ticker}: {e}")
        return None

def invested(buy, qty):
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    try:
        return qty * buy
    except Exception as e:
        print(f"Error calculating invested amount: {e}")
        return None

def telegram(token, id, message):
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            "chat_id": id,
            "text": message
        }
        response = requests.post(url, data=data)
        return response.json()
    except Exception as e:
        print(f"Error sending message via Telegram: {e}")
        return None

def ychart(ticker):
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    link = "https://finance.yahoo.com/chart/" + ticker.upper()
    webbrowser.open_new(link)

def ynews(ticker):
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    link = "https://finance.yahoo.com/news/"
    webbrowser.open_new(link)

def change(pair):
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    try:
        currency_pair = yf.Ticker(pair.upper() + "=X")
        data = currency_pair.history(period="1d")
        exchange_rate = data['Close'].iloc[-1]
        return exchange_rate
    except Exception as e:
        print(f"Error fetching exchange rate for {pair}: {e}")
        return None

def ath(ticker):
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="max")
        ath = data['Close'].max()
        return ath
    except Exception as e:
        print(f"Error fetching ATH for {ticker}: {e}")
        return None

def get_currency(ticker):
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    try:
        stock = yf.Ticker(ticker)
        currency = stock.info['currency']
        return currency.upper()
    except Exception as e:
        print(f"Error fetching currency for {ticker}: {e}")
        return None

def get_exchange(ticker):
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        exchange = info.get('exchange')
        return exchange
    except Exception as e:
        print(f"Error fetching exchange for {ticker}: {e}")
        return None
    
def clean():
    import yfinance as yf
    import requests
    import webbrowser
    import ta
    import pandas as pd
    import time
    import os
    os.system("cls")
    os.system("clear")