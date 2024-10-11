# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
# https://github.com/pandas-dev/pandas/pull/18921
# minp=0
x = Series([np.nan])
result = x.expanding(min_periods=0).sum()
expected = Series([0.0])
tm.assert_series_equal(result, expected)

# minp=1
result = x.expanding(min_periods=1).sum()
expected = Series([np.nan])
tm.assert_series_equal(result, expected)
