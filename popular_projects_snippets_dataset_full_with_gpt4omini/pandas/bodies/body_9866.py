# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH: 31286
x = Series([1, 2, 3, 4, 5], index=index)
y = x.copy()
x.iloc[0:2] = 0.0
result = x.rolling(window).corr(y)
expected = Series([np.nan, np.nan, 1, 1, 1], index=index)
tm.assert_almost_equal(result, expected)
