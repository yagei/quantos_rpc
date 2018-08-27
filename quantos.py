#!/usr/local/bin/python3.7

from flask import flask,request

from opendatatools import stock

    # ,fx,futures,fund,hsgt,economy,aqi,coin,gaokao,movie,realestate,spot

app = flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/stock/get_daily", methods=['POST'])
def stock_get_daily():
    df, msg = stock.get_daily(symbol=request.form['symbol'], start_date=request.form['start_date'], end_date=request.form['end_date'])
    return df.to_json(orient='table')

@app.route("/stock/get_quote", methods=['POST'])
def get_quote():
    df, msg = stock.get_quote(symbols=request.form['symbols'])
    return df.to_json(orient='table')

@app.route("/stock/get_kline", methods=['POST'])
def get_kline():
    df, msg = stock.get_kline(symbol=request.form['symbol'], trade_date=request.form['trade_date'], period=request.form['period'])
    return df.to_json(orient='table')


@app.route("/stock/get_adj_factor", methods=['POST'])
def get_adj_factor():
    df, msg = stock.get_adj_factor(symbol=request.form['symbol'])
    return df.to_json(orient='table')

@app.route("/stock/get_trade_detail", methods=['POST'])
def get_trade_detail():
    df, msg = stock.get_trade_detail(symbol=request.form['symbol'],trade_date=request.form['trade_date'])
    return df.to_json(orient='table')

@app.route("/stock/get_index_list", methods=['POST'])
def get_index_list():
    df, msg = stock.get_index_list(market=request.form['market'])
    return df.to_json(orient='table')


@app.route("/stock/get_index_component", methods=['POST'])
def get_index_component():
    df, msg = stock.get_index_component(symbol=request.form['symbol'])
    return df.to_json(orient='table')

@app.route("/stock/get_rzrq_info", methods=['POST'])
def get_rzrq_info():
    df, msg = stock.get_rzrq_info(market=request.form['market'],date=request.form['date'])
    return df.to_json(orient='table')

@app.route("/stock/get_dividend", methods=['POST'])
def get_dividend():
    df, msg = stock.get_dividend(symbol=request.form['symbol'])
    return df.to_json(orient='table')



@app.route("/stock/get_pledge_info", methods=['POST'])
def get_pledge_info():
    df, msg = stock.get_pledge_info(market=request.form['market'],date=request.form['date'])
    return df.to_json(orient='table')



@app.route("/stock/get_report_data", methods=['POST'])
def get_report_data():
    df, msg = stock.get_report_data(symbol=request.form['symbol'],type=request.form['type'])
    return df.to_json(orient='table')


@app.route("/stock/get_shareholder_structure", methods=['POST'])
def get_shareholder_structure():
    df, msg = stock.get_shareholder_structure(symbol=request.form['symbol'])
    return df.to_json(orient='table')



@app.route("/stock/get_realtime_money_flow", methods=['POST'])
def get_realtime_money_flow():
    df, msg = stock.get_realtime_money_flow(symbol=request.form['symbol'])
    return df.to_json(orient='table')


@app.route("/stock/get_hist_money_flow", methods=['POST'])
def get_hist_money_flow():
    df, msg = stock.get_hist_money_flow(symbol=request.form['symbol'])
    return df.to_json(orient='table')


@app.route("/stock/get_hist_money_flow_market", methods=['POST'])
def get_hist_money_flow_market():
    df, msg = stock.get_hist_money_flow_market()
    return df.to_json(orient='table')


@app.route("/stock/get_realtime_money_flow_market", methods=['POST'])
def get_realtime_money_flow_market():
    df, msg = stock.get_realtime_money_flow_market()
    return df.to_json(orient='table')


if __name__ == "__main__":
    app.run()
