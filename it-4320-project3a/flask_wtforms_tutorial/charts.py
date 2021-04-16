'''
This web service extends the Alphavantage api by creating a visualization module, 
converting json query results retuned from the api into charts and other graphics. 

This is where you should add your code to function query the api
'''
import requests, pygal, lxml
from datetime import datetime
from datetime import date
import numpy
import alpha_vantage
import time
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

#Helper function for converting date
def convert_date(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d').date()

API_URL = "https://www.alphavantage.co/query"
API_KEY = "X0AWJSYKTOKX2F5E"

def getData(symbol, timeSeries, chartType, startDate, endDate):

    ts = TimeSeries(key=API_KEY, output_format='pandas')
    if timeSeries == '1':
        data, meta_data = ts.get_intraday(symbol=symbol, interval='60min', outputsize='full')
        f = 'H'
    if timeSeries == '2':
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')
        f = 'D'
    if timeSeries == '3':
        data, meta_data = ts.get_weekly(symbol=symbol)
        f = 'W'
    if timeSeries == '4':
        data, meta_data = ts.get_monthly(symbol=symbol)
        f = 'M'

    data_date_changed = data[endDate:startDate]

    if chartType == "1":
        line_chart = pygal.Bar(x_label_rotation=20, width=1000, height = 400)
        line_chart.title = 'Stock Data for {}:  {} to {}'.format(symbol, startDate, endDate)
        labels = data_date_changed.index.to_list()
        line_chart.x_labels= reversed(labels)
        line_chart.add("Open", data_date_changed['1. open'])
        line_chart.add("High", data_date_changed['2. high'])
        line_chart.add("Low", data_date_changed['3. low'])
        line_chart.add("Close", data_date_changed['4. close'])
        line_chart.render_in_browser()

    if chartType == "2":
        line_chart = pygal.Line(x_label_rotation=20, width=1000, height = 400)
        line_chart.title = 'Stock Data for {}: {} to {}'.format(symbol, startDate, endDate)
        labels = data_date_changed.index.to_list()
        line_chart.x_labels= reversed(labels)
        line_chart.add("Open", data_date_changed['1. open'])
        line_chart.add("High", data_date_changed['2. high'])
        line_chart.add("Low", data_date_changed['3. low'])
        line_chart.add("Close", data_date_changed['4. close'])
        line_chart.render_in_browser()

#Function that checks for errors in the date entries
def dCheck(startDate, endDate):
    #Checks for execptions in to make sure user entered dates are in correct format
    try:
        #Converts user entered dates in to readable values
        sDate = time.mktime(time.strptime(startDate, "%Y-%m-%d"))
        eDate = time.mktime(time.strptime(endDate, "%Y-%m-%d"))
        #Checks if end date given is before current date
        if(eDate > time.time()):
            print("\nERROR: End date can not be after the current date.")
            return False
        #Checks if start date given is before the given end date
        if(sDate < eDate):
            return True
        else:
            print("\nERROR: Start date must be before the end date.")
            return False
    except:
        print("\nERROR: One, or both, of the given dates are not acceptable, try again.")
        return False
