# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH: 37557
s = Series([3000000, 1, 1, 2, 3, 4, 999])
result = getattr(s.rolling(4), method)()
expected = Series([np.nan] * 3 + values)
tm.assert_series_equal(result, expected)
