# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
ser = Series(np.nan, index=[0, 1, 2])
result = ser.fillna(999, limit=1)
expected = Series([999, np.nan, np.nan], index=[0, 1, 2])
tm.assert_series_equal(result, expected)

result = ser.fillna(999, limit=2)
expected = Series([999, 999, np.nan], index=[0, 1, 2])
tm.assert_series_equal(result, expected)
