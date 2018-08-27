#!/usr/local/bin/python3.6

from flask import Flask,request

from opendatatools import fx,stock,futures,fund,hsgt,economy,aqi,coin,gaokao,movie,realestate,spot

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/stock/get_daily", methods=['GET', 'POST'])
def stock_get_daily():
    df, msg = stock.get_daily(symbol=request.form['symbol'], start_date=request.form['start_date'], end_date=request.form['end_date'])
    return df.to_json(orient='table')

    return ''

if __name__ == "__main__":
    app.run()
