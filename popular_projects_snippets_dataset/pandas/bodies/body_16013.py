# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
# https://github.com/pandas-dev/pandas/issues/37094
# combination of object dtype for the values and > 1_000_000 elements
ser = Series([1, 2, np.nan] * 1_000_000)
result = ser.isin({"foo", "bar"})
expected = Series([False] * 3 * 1_000_000)
tm.assert_series_equal(result, expected)
