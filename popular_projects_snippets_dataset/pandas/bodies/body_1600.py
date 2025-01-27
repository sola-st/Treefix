# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#20393
ser = Series(range(11), timedelta_range("0 days", "10 days"))
result = ser.loc[slice(start, stop)]
expected = ser.iloc[expected_slice]
tm.assert_series_equal(result, expected)
