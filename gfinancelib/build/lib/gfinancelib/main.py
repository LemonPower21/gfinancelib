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
    from colorama import init, Fore
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
    from colorama import init, Fore
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
    from colorama import init, Fore
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
    from colorama import init, Fore
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
    from colorama import init, Fore
    def check_network():
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        dev_null = 'NUL' if platform.system().lower() == 'windows' else '/dev/null'
        response = os.system(f"ping {param} 1 8.8.8.8 > {dev_null} 2>&1")
        return response == 0
    while not check_network():
        waitvar = 0
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
    from colorama import init, Fore
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
    from colorama import init, Fore
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
    from colorama import init, Fore
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
    from colorama import init, Fore
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
    from colorama import init, Fore
    def check_network():
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        dev_null = 'NUL' if platform.system().lower() == 'windows' else '/dev/null'
        response = os.system(f"ping {param} 1 8.8.8.8 > {dev_null} 2>&1")
        return response == 0
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
                    f"attachment; filename={filename}",
                )
                msg.attach(part)
            with smtplib.SMTP(server, port) as smtp:
                smtp.starttls()
                smtp.login(user, password)
                smtp.send_message(msg)
            break
        except Exception as e:
            time.sleep(5)
def ychart(ticker):
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
    from colorama import init, Fore
    brows = input("Do you want chart (Y/N) :> ").upper()
    if(brows == "Y"):
        t = ticker.upper()
        link = f"https://finance.yahoo.com/chart/{t}"
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
    from colorama import init, Fore
    link = "https://finance.yahoo.com/news/"
    news = input("Do you want news (Y/N) :> ").upper()
    if(news == "Y"):
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
    from colorama import init, Fore
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
    from colorama import init, Fore
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
    from colorama import init, Fore
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
    from colorama import init, Fore
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
    from colorama import init, Fore
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
    from colorama import init, Fore
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
    from colorama import init, Fore
    try:
        stock = yf.Ticker(ticker)
        shares_outstanding = stock.info.get('sharesOutstanding', None)
        return shares_outstanding
    except Exception as e:
        return None
def invested(qty,buyprice):
    try:
        return qty*buyprice
    except Exception as e:
        return None
def roi(buyprice,lastprice):
    try:
        return ((lastprice-buyprice)/buyprice)*100
    except Exception as e:
        return None
def pandl(roiperc,invested):
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
    from colorama import init, Fore
    try:
        return (roiperc/100)*invested
    except Exception as e:
        return None
def initprint():
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
    from colorama import init, Fore
    print(f"{Fore.CYAN}{'Ticker':<10}\t{'Exchange':<10}\t{'Currency':<10}\t{'Change':<10}\t{'Quantity':<10}\t{'Invested':<10}\t{'Buy':<10}\t{'Last':<10}\t{'TP(%)':<10}\t{'P&L(%)':<10}\t{'P&L(€)':<10}\t{'EMA':<10}\t{'RSI':<10}\t{'ATH':<10}\t{'Bid':<10}\t{'Ask':<10}\t{'Spread':<10}\t{'Shares':<10}\t{'Volume':<15}\t{'MarketCap':<20}\t{'Elapsed time':<30}{Fore.RESET}")
def printall(tickerv, lastv, exchangev, currencyv, changev, emav, rsiv, athv,bidv,askv,volumev,marketcapv,sharesv,qtyv=0, investedv=0, buyv=0, tpv=0, roiv=0, profitv=0, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
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
    from colorama import init, Fore
    def color_value(value):
        if value > 0: 
            return Fore.GREEN  
        if value < 0: 
            return Fore.RED
        return Fore.RESET    
    def color_ema(emav, lastv):
        return Fore.GREEN if emav > lastv else Fore.RED
    def color_rsi(rsiv):
        if rsiv < 30:
            return Fore.GREEN 
        elif rsiv > 70:
            return Fore.RED    
        return Fore.YELLOW 
    tpv_str = f"{tpv:.2f}%"
    roiv_str = f"{roiv:.2f}%"
    profitv_str = f"{profitv:.2f}€"
    print(f"{Fore.MAGENTA}{tickerv:<10}{Fore.RESET}\t{Fore.BLUE}{exchangev:<10}{Fore.RESET}\t{currencyv:<10}\t{changev:<10.4f}\t{qtyv:<10.2f}\t{investedv:<10.2f}\t{buyv:<10.2f}\t{lastv:<10.2f}\t{tpv_str:<10}\t{color_value(roiv)}{roiv_str:<10}{Fore.RESET}\t{color_value(profitv)}{profitv_str:<10}{Fore.RESET}\t{color_ema(emav, lastv)}{emav:<10.2f}{Fore.RESET}\t{color_rsi(rsiv)}{rsiv:<10.2f}{Fore.RESET}\t{athv:<10.2f}\t{Fore.BLUE}{bidv:<10.2f}{Fore.RESET}\t{Fore.YELLOW}{askv:<10.2f}{Fore.RESET}\t{askv-bidv:<10.2f}\t{sharesv:<10.2f}\t{volumev:<10.2f}\t{marketcapv:<10.2f}\t{years}Y, {months}M, {days}d, {hours}h, {minutes}m, {seconds:.2f}s")