# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# GH 6424
df = Series([1, np.nan, 3], index=pd.to_timedelta([1, 2, 3]))
result = df.interpolate(method="time")
expected = Series([1.0, 2.0, 3.0], index=pd.to_timedelta([1, 2, 3]))
tm.assert_series_equal(result, expected)

# test for non uniform spacing
df = Series([1, np.nan, 3], index=pd.to_timedelta([1, 2, 4]))
result = df.interpolate(method="time")
expected = Series([1.0, 1.666667, 3.0], index=pd.to_timedelta([1, 2, 4]))
tm.assert_series_equal(result, expected)
