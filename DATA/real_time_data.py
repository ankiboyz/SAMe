# real_time_data.py
"""
This file is supposed to get the real time data.
This have multiple methods corresponding to the source of the data.
"""
import yfinance as yf
from datetime import datetime

def real_time_data_yf(ticker, start_date, end_date, interval):
    '''
    This method makes a real time call to the yahoo finance library to gather the data.
    input :
        start datetime
        end datetime
        interval.
    yf library is not able to accept the datetime parameter for start and end datetime.
    So , it will be a needed thing to have a data structure where in all the historical prices etc. are loaded.
    per granularity the max it can achieve minute wise etc.
    And then based on the data needed it can roll up as needed.
    For yf; the minute wise interval is supported ONLY if the start date is within the last 60 days.

    Here, the needed thing is that the provided ticker is recognised by the yfinance lib.

    https://github.com/ranaroussi/yfinance/blob/1297cd10e878c8984de157dfa3cedf2a1694379e/yfinance/multi.py#L32
    This is the download information:
    def download(tickers, start=None, end=None, actions=False, threads=True,
             group_by='column', auto_adjust=False, back_adjust=False,
             progress=True, period="max", show_errors=True, interval="1d", prepost=False,
             proxy=None, rounding=False, timeout=None, **kwargs):
    """Download yahoo tickers
    :Parameters:
        tickers : str, list
            List of tickers to download
        period : str
            Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            Either Use period parameter or use start and end
        interval : str
            Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            Intraday data cannot extend last 60 days
        start: str
            Download start date string (YYYY-MM-DD) or _datetime.
            Default is 1900-01-01
        end: str
            Download end date string (YYYY-MM-DD) or _datetime.
            Default is now
        group_by : str
            Group by 'ticker' or 'column' (default)
        prepost : bool
            Include Pre and Post market data in results?
            Default is False
        auto_adjust: bool
            Adjust all OHLC automatically? Default is False
        actions: bool
            Download dividend + stock splits data. Default is False
        threads: bool / int
            How many threads to use for mass downloading. Default is True
        proxy: str
            Optional. Proxy server URL scheme. Default is None
        rounding: bool
            Optional. Round values to 2 decimal places?
        show_errors: bool
            Optional. Doesn't print errors if True
        timeout: None or float
            If not None stops waiting for a response after given number of
            seconds. (Can also be a fraction of a second e.g. 0.01)
    '''

    # Verifying if the ticker is a valid ticker for the yfinance library.
    # This validation whether the ticker is available needs to be done.

    # Validations that needs to be done here is:
    # 1. If the start date is beyond 60 days of the current day then the interval cannot be in minutes;
    #    current limitation of yfinance.
    # 2. The start date and the end date need to be of the format YYYY-MM-DD
    #    (i.e. strptime format of %Y-%m-%d datetime.strptime(date_string_b, '%Y-%m-%d')
    # 3.

    # Here, we call the
    try:
        start_datetime = datetime.strptime(start_date, '%Y-%m-%d')

    except:
        flag_datetime_format_violation


