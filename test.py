#!/usr/local/bin/python3.6

from opendatatools import fx,stock,futures,fund,hsgt,economy,aqi,coin,gaokao,movie,realestate,spot


df, msg = stock.get_daily('600000.SH', start_date='2018-06-20', end_date='2018-08-27')

print(df)

#
#df = fx.get_cny_spot_price()
#print(df)
#
#df = coin.get_coin_price('BTC','USD,ETH,EOS')
#print(df)