# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH: 37051
ds = Series([99999999999999999, 1, third_value, 2, 3, 1, 1])
result = getattr(ds.rolling(2), func)()
expected = Series([np.nan] + values)
tm.assert_series_equal(result, expected)
# GH 42064
# new `roll_var` will output 0.0 correctly
tm.assert_series_equal(result == 0, expected == 0)
