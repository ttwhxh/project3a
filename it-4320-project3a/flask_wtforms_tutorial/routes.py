from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import StockForm
from .charts import *


@app.route("/", methods=['GET', 'POST'])
@app.route("/stocks", methods=['GET', 'POST'])
def stocks():
    
    form = StockForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            #Get the form data to query the api
            symbol = request.form['symbol']
            chart_type = request.form['chart_type']
            time_series = request.form['time_series']
            start_date = convert_date(request.form['start_date'])
            end_date = convert_date(request.form['end_date'])

            if end_date <= start_date:
                #Generate error message as pass to the page
                err = "ERROR: End date cannot be earlier than Start date."
                chart = None
            else:
                #query the api using the form data
                err = None
                 
                #THIS IS WHERE YOU WILL CALL THE METHODS FROM THE CHARTS.PY FILE AND IMPLEMENT YOUR CODE

def main():
    #Lists of the acceptable options for the chart types and time series inputs
    chartOptions = ("1", "2")
    seriesOptions = ("1", "2", "3", "4")
    
    while(True):
        try:
            
            print("Stock Data Visualizer")
            print("-------------------------")
            symbol = input("Enter the stock symbol you are looking for: ")

            #Repeats prompt if user input is unacceptable
            while(True):
                print("\nChart Type:")
                print("-------------------------")
                print("1. Bar\n2. Line\n")
                chartType = input("Enter the chart type you want (1,2): ")
                #Checks user input against options list
                if (chartType in chartOptions):
                    break
                print("\nERROR: Input not acceptable, try again.")

            #Repeats prompt if user input is unacceptable
            while(True):
                print("\nSelect the time series of the chart you want to generate")
                print("-------------------------------------------------------------")
                print("1.Intrady\n2. Daily\n3. Weekly\n4. Monthly")
                timeSeries = input("Enter time series option (1,2,3,4): ")
                #Checks user input against options list
                if (timeSeries in seriesOptions):
                    break
                print("\nERROR: Input not acceptable, try again.")

            #Repeats both date entry promts if user input is unacceptable
            while(True):
                startDate = input("\nEnter the start date (YYYY-MM-DD): ")
                endDate = input("\nEnter the end date (YYYY-MM-DD): ")
                #Send dates to be checked in the dCheck method
                if(dCheck(startDate, endDate)):
                    break
            
            getData(symbol, timeSeries, chartType, startDate, endDate)

        #Moved except clause so its code is executed before the prompted to end the loop
        except Exception as err:
            print("\nERROR: ", err.__class__)

        again = input("\nWould you like to view more stock data? Press 'y' to continue: ")
        print(" ")
        if (again.lower() != "y"):
            break
            

main()
                
                #This chart variable is what is passed to the stock.html page to render the chart returned from the api
                
chart = "ASSIGN CHART TO THIS VARIABLE"

return render_template("stock.html", form=form, template="form-template", err = err, chart = chart)
    
return render_template("stock.html", form=form, template="form-template")
