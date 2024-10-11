# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
# Define a TradingDay offset
holidays = ["2012-05-01", datetime(2013, 5, 1), np.datetime64("2014-05-01")]
tday = CDay(holidays=holidays)
for year in range(2012, 2015):
    dt = datetime(year, 4, 30)
    xp = datetime(year, 5, 2)
    rs = dt + tday
    assert rs == xp
