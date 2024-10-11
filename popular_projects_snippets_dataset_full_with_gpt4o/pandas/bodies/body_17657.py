# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
# Define a TradingDay offset
holidays = ["2012-01-31", datetime(2012, 2, 28), np.datetime64("2012-02-29")]
bm_offset = CBMonthEnd(holidays=holidays)
dt = datetime(2012, 1, 1)
assert dt + bm_offset == datetime(2012, 1, 30)
assert dt + 2 * bm_offset == datetime(2012, 2, 27)
