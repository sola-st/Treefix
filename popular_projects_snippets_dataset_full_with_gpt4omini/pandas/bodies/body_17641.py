# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
# Define a TradingDay offset
holidays = ["2012-02-01", datetime(2012, 2, 2), np.datetime64("2012-03-01")]
bm_offset = CBMonthBegin(holidays=holidays)
dt = datetime(2012, 1, 1)

assert dt + bm_offset == datetime(2012, 1, 2)
assert dt + 2 * bm_offset == datetime(2012, 2, 3)
