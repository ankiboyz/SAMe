# real_time_data.py
"""
This file is supposed to get the real time data.
This have multiple methods corresponding to the source of the data.
"""
import yfinance as yf

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
    '''

