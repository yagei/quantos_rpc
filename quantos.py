#!/usr/local/bin/python3.7

from flask import Flask,request

from opendatatools import stock,fx,futures,fund,hsgt,economy,usstock,hedgefund,swindex,nhindex,shippingindex,index,aqi,coin,gaokao,movie,sns,realestate,spot,worldcup

from pprint import pprint

import json

# html5lib xlrd


app = Flask(__name__)

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
    df = stock.get_index_list(market=request.form['market'])
    return df.to_json(orient='table')


@app.route("/stock/get_index_component", methods=['POST'])
def get_index_component():
    df = stock.get_index_component(symbol=request.form['symbol'])
    return df.to_json(orient='table')

@app.route("/stock/get_rzrq_info", methods=['POST'])
def get_rzrq_info():
    df, msg = stock.get_rzrq_info(market=request.form['market'],date=request.form['date'])
    return df.to_json(orient='table')

@app.route("/stock/get_dividend", methods=['POST'])
def get_dividend():
    df = stock.get_dividend(symbol=request.form['symbol'])
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










@app.route("/futures/get_trade_rank", methods=['POST'])
def futures_get_trade_rank():
    df, msg = futures.get_trade_rank(market = request.form['market'], date = request.form['date'])
    return df.to_json(orient='table')


@app.route("/futures/get_quote", methods=['POST'])
def futures_get_quote():
    df, msg = futures.get_quote(codes = request.form['codes'])
    return df.to_json(orient='table')


@app.route("/futures/get_kline", methods=['POST'])
def futures_get_kline():
    df, msg = futures.get_kline(type = request.form['type'],code = request.form['code'])
    return df.to_json(orient='table')










@app.route("/fx/get_hist_cny_cpr", methods=['POST'])
def fx_get_hist_cny_cpr():
    df, msg = fx.get_hist_cny_cpr(start_date=request.form['start_date'], end_date=request.form['end_date'])
    return df.to_json(orient='table')

@app.route("/fx/get_his_shibor", methods=['POST'])
def fx_get_his_shibor():
    df, msg = fx.get_his_shibor(start_date=request.form['start_date'], end_date=request.form['end_date'])
    return df.to_json(orient='table')

@app.route("/fx/get_realtime_shibor", methods=['POST'])
def fx_get_realtime_shibor():
    df= fx.get_realtime_shibor()
    return df.to_json(orient='table')

@app.route("/fx/get_cny_spot_price", methods=['POST'])
def fx_get_cny_spot_price():
    df= fx.get_cny_spot_price()
    return df.to_json(orient='table')

@app.route("/fund/get_fund_company", methods=['POST'])
def fund_get_fund_company():
    df ,msg = fund.get_fund_company()
    return df.to_json(orient='table')

@app.route("/fund/get_fundlist_by_company", methods=['POST'])
def fund_get_fundlist_by_company():
    df ,msg = fund.get_fundlist_by_company(companyid=request.form['companyid'])
    return df.to_json(orient='table')

@app.route("/fund/get_fund_type", methods=['POST'])
def fund_get_fund_type():
    df = fund.get_fund_type()
    return json.dumps(list(df))

@app.route("/fund/get_fundlist_by_type", methods=['POST'])
def fund_get_fundlist_by_type():
    df ,msg = fund.get_fundlist_by_type(type=request.form['type'])
    return df.to_json(orient='table')

@app.route("/fund/get_fund_nav", methods=['POST'])
def fund_get_fund_nav():
    df ,msg = fund.get_fund_nav(fund_code=request.form['fund_code'])
    return df.to_json(orient='table')

@app.route("/fund/get_fund_list", methods=['POST'])
def fund_get_fund_list():
    df ,msg = fund.get_fund_list()
    return df.to_json(orient='table')












@app.route("/economy/get_region_map", methods=['POST'])
def economy_get_region_map():
    df = economy.get_region_map()
    return df.to_json(orient='table')

@app.route("/economy/get_indicator_map", methods=['POST'])
def economy_get_indicator_map():
    df = economy.get_indicator_map()
    return df.to_json(orient='table')

@app.route("/economy/get_city_map", methods=['POST'])
def economy_get_city_map():
    df = economy.get_city_map()
    return df.to_json(orient='table')

@app.route("/economy/get_gdp_y", methods=['POST'])
def economy_get_gdp_y():
    df ,msg = economy.get_gdp_y()
    return df.to_json(orient='table')

@app.route("/economy/get_population_size_y", methods=['POST'])
def economy_get_population_size_y():
    df ,msg = economy.get_population_size_y()
    return df.to_json(orient='table')

@app.route("/economy/get_population_structure_y", methods=['POST'])
def economy_get_population_structure_y():
    df ,msg = economy.get_population_structure_y()
    return df.to_json(orient='table')

@app.route("/economy/get_gdp", methods=['POST'])
def economy_get_gdp():
    df ,msg = economy.get_gdp()
    return df.to_json(orient='table')

@app.route("/economy/get_gdp_q2q", methods=['POST'])
def economy_get_gdp_q2q():
    df ,msg = economy.get_gdp_q2q()
    return df.to_json(orient='table')

@app.route("/economy/get_region_gdp", methods=['POST'])
def economy_get_region_gdp():
    df ,msg = economy.get_region_gdp(region=request.form['region'])
    return df.to_json(orient='table')

@app.route("/economy/get_cpi", methods=['POST'])
def economy_get_cpi():
    df ,msg = economy.get_cpi()
    return df.to_json(orient='table')

@app.route("/economy/get_ppi", methods=['POST'])
def economy_get_ppi():
    df ,msg = economy.get_ppi()
    return df.to_json(orient='table')

@app.route("/economy/get_region_ppi", methods=['POST'])
def economy_get_region_ppi():
    df ,msg = economy.get_region_ppi(region=request.form['region'])
    return df.to_json(orient='table')

@app.route("/economy/get_manufacturing_pmi", methods=['POST'])
def economy_get_manufacturing_pmi():
    df ,msg = economy.get_manufacturing_pmi()
    return df.to_json(orient='table')

@app.route("/economy/get_non_manufacturing_pmi", methods=['POST'])
def economy_get_non_manufacturing_pmi():
    df ,msg = economy.get_non_manufacturing_pmi()
    return df.to_json(orient='table')

@app.route("/economy/get_import_export", methods=['POST'])
def economy_get_import_export():
    df ,msg = economy.get_import_export()
    return df.to_json(orient='table')

@app.route("/economy/get_fdi", methods=['POST'])
def economy_get_fdi():
    df ,msg = economy.get_fdi()
    return df.to_json(orient='table')

@app.route("/economy/get_fiscal_revenue", methods=['POST'])
def economy_get_fiscal_revenue():
    df ,msg = economy.get_fiscal_revenue()
    return df.to_json(orient='table')

@app.route("/economy/get_fiscal_expend", methods=['POST'])
def economy_get_fiscal_expend():
    df ,msg = economy.get_fiscal_expend()
    return df.to_json(orient='table')

@app.route("/economy/get_M0_M1_M2", methods=['POST'])
def economy_get_M0_M1_M2():
    df ,msg = economy.get_M0_M1_M2()
    return df.to_json(orient='table')

@app.route("/economy/get_fixed_asset_investment", methods=['POST'])
def economy_get_fixed_asset_investment():
    df ,msg = economy.get_fixed_asset_investment()
    return df.to_json(orient='table')

@app.route("/economy/get_realestate_investment", methods=['POST'])
def economy_get_realestate_investment():
    df ,msg = economy.get_realestate_investment()
    return df.to_json(orient='table')

@app.route("/economy/get_retail_sales", methods=['POST'])
def economy_get_retail_sales():
    df ,msg = economy.get_retail_sales()
    return df.to_json(orient='table')

@app.route("/economy/get_online_retail_sales", methods=['POST'])
def economy_get_online_retail_sales():
    df ,msg = economy.get_online_retail_sales()
    return df.to_json(orient='table')

@app.route("/economy/get_house_price_index", methods=['POST'])
def economy_get_house_price_index():
    df ,msg = economy.get_house_price_index(region=request.form['region'])
    return df.to_json(orient='table')










@app.route("/hsgt/get_lgt_share", methods=['POST'])
def hsgt_get_lgt_share():
    df  = hsgt.get_lgt_share(market=request.form['market'], date=request.form['date'])
    return df.to_json(orient='table')

@app.route("/hsgt/get_realtime_moneyflow", methods=['POST'])
def hsgt_get_realtime_moneyflow():
    df ,msg = hsgt.get_realtime_moneyflow()
    return df.to_json(orient='table')

@app.route("/hsgt/get_hist_moneyflow", methods=['POST'])
def hsgt_get_hist_moneyflow():
    df ,msg = hsgt.get_hist_moneyflow()
    return df.to_json(orient='table')

@app.route("/hsgt/get_his_tradestat", methods=['POST'])
def hsgt_get_his_tradestat():
    df ,msg = hsgt.get_his_tradestat(markettype=int(request.form['markettype']))
    return df.to_json(orient='table')

@app.route("/hsgt/get_ah_compare", methods=['POST'])
def hsgt_get_ah_compare():
    df ,msg = hsgt.get_ah_compare()
    return df.to_json(orient='table')









@app.route("/usstock/get_symbols", methods=['POST'])
def usstock_get_symbols():
    df ,msg = usstock.get_symbols()
    return df.to_json(orient='table')

@app.route("/usstock/get_daily", methods=['POST'])
def usstock_get_daily():
    df ,msg = usstock.get_daily(symbol=request.form['symbol'])
    return df.to_json(orient='table')

@app.route("/usstock/get_dividend", methods=['POST'])
def usstock_get_dividend():
    df ,msg = usstock.get_dividend(symbol=request.form['symbol'])
    return df.to_json(orient='table')

@app.route("/usstock/get_split", methods=['POST'])
def usstock_get_split():
    df ,msg = usstock.get_split(symbol=request.form['symbol'])
    return df.to_json(orient='table')















if __name__ == "__main__":
    app.run(debug=True)
