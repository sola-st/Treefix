# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 5152
dates = [datetime(2013, 10, 7), datetime(2013, 10, 8), datetime(2013, 10, 9)]
data = DatetimeIndex(dates, freq=offsets.BDay()).values
result = DatetimeIndex(data, freq=offsets.BDay())
expected = DatetimeIndex(["2013-10-07", "2013-10-08", "2013-10-09"], freq="B")
tm.assert_index_equal(result, expected)
