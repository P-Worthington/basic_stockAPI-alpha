from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='5MT4XVRROBUGFRHZ')

data = ts.get_intraday('GOOGL')

print(data)