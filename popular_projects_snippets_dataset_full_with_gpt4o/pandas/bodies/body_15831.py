# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rank.py
method, exp = results
s = ser.dropna().astype("i8")

result = s.rank(method=method)
expected = Series(exp).dropna()
expected.index = result.index
tm.assert_series_equal(result, expected)
