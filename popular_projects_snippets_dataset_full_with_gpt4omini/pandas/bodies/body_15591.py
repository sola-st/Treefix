# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
x = Series([np.nan, 1.0, np.nan, 3.0, np.nan], ["z", "a", "b", "c", "d"])
y = x.copy()

return_value = y.fillna(value=0, inplace=True)
assert return_value is None

expected = x.fillna(value=0)
tm.assert_series_equal(y, expected)
