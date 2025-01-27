# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rank.py
method, exp = results
ser = ser if dtype is None else ser.astype(dtype)
result = ser.rank(method=method)
tm.assert_series_equal(result, Series(exp))
