def bid(ticker):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    try:
        stock = yf.Ticker(ticker.upper())
        ask_price = stock.info.get('bid', None)
        if ask_price:
            return ask_price
        else:
            return 0
    except Exception as e:
        return None
def ask(ticker):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    try:
        stock = yf.Ticker(ticker.upper())
        ask_price = stock.info.get('ask', None)
        if ask_price:
            return ask_price
        else:
            return 0
    except Exception as e:
        return None
def start():
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    return time.time()
def stop(start):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    elapsed_time = time.time() - start
    years = int(elapsed_time // (365.25 * 24 * 3600))
    elapsed_time %= (365.25 * 24 * 3600)
    months = int(elapsed_time // (30.44 * 24 * 3600)) 
    elapsed_time %= (30.44 * 24 * 3600)
    days = int(elapsed_time // (24 * 3600))
    elapsed_time %= (24 * 3600)
    hours = int(elapsed_time // 3600)
    elapsed_time %= 3600
    minutes = int(elapsed_time // 60)
    seconds = elapsed_time % 60
    return years, months, days, hours, minutes, seconds
def log(text):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    def check_network():
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        return os.system(f"ping {param} 1 8.8.8.8") == 0
    while not check_network():
        print("Network error...")
    current_time = datetime.datetime.now(datetime.timezone.utc).astimezone().strftime('%Y-%m-%d %H:%M:%S')
    with open("log.txt", 'a') as file:
        file.write(f"\nLOGGER SYSTEM UPDATE [{current_time}]\n{text}\n")
def last(ticker):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    try:
        return yf.Ticker(ticker).history(period="1d", interval="1m").iloc[-1]['Close']
    except Exception:
        return None
def rsi(ticker, periods, chart, timeframe):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    try:
        data = yf.Ticker(ticker).history(period=chart, interval=timeframe)
        data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=periods).rsi()
        return data['RSI'].iloc[-1]
    except Exception:
        return None
def ema(ticker, periods, chart, timeframe):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    try:
        data = yf.Ticker(ticker).history(period=chart, interval=timeframe)
        return data['Close'].ewm(span=periods, adjust=False).mean().iloc[-1]
    except Exception:
        return None
def clean():
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    os.system('cls' if platform.system() == 'Windows' else 'clear')
def email(server, port, user, password, recipient, subject, body):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    clean()
    def check_network():
        clean()
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        return os.system(f"ping {param} 1 8.8.8.8") == 0
    while True:
        try:
            while not check_network():
                time.sleep(5)
            msg = MIMEMultipart()
            msg['From'] = user
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            filename = "log.txt"
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {filename}",
                )
                msg.attach(part)
            with smtplib.SMTP(server, port) as smtp:
                smtp.starttls()
                smtp.login(user, password)
                smtp.send_message(msg)
            break
        except Exception as e:
            time.sleep(5)
def ychart():
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    link = "https://finance.yahoo.com/chart/LIVE"
    webbrowser.open_new(link)
def ynews():
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    link = "https://finance.yahoo.com/news/"
    webbrowser.open_new(link)
def change(pair):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    try:
        currency_pair = yf.Ticker(pair.upper() + "EUR=X")
        if (currency_pair == "EUREUR"):
            return 1
        else:
            data = currency_pair.history(period="1d")
            exchange_rate = data['Close'].iloc[-1]
            return exchange_rate
    except Exception as e:
        return None
def ath(ticker):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="max")
        ath = data['Close'].max()
        lastv = last(ticker)
        if(lastv>ath):
            return lastv
        else:
            return ath
    except Exception as e:
        return None
def currency(ticker):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    try:
        stock = yf.Ticker(ticker)
        currency = stock.info['currency']
        return currency.upper()
    except Exception as e:
        return None
def exchange(ticker):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        exchange = info.get('exchange')
        return exchange
    except Exception as e:
        return None
def volume(ticker):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    try:
        stock = yf.Ticker(ticker)
        real_time_volume = stock.info.get('regularMarketVolume', None)
        return real_time_volume
    except Exception as e:
        return None
def marketcap(ticker):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    try:
        stock = yf.Ticker(ticker)
        market_cap = stock.info.get('marketCap', None)
        return market_cap
    except Exception as e:
        return None
def shares(ticker):
    import yfinance as yf
    import ta
    import time
    import os
    import platform
    import webbrowser
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import datetime
    try:
        stock = yf.Ticker(ticker)
        shares_outstanding = stock.info.get('sharesOutstanding', None)
        return shares_outstanding
    except Exception as e:
        return None