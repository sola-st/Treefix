# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
ser = Series([np.nan, 1.0, np.nan, 3.0, np.nan], ["z", "a", "b", "c", "d"])
filled = ser.fillna(method="ffill")
expected = Series([np.nan, 1.0, 1.0, 3.0, 3.0], ser.index)
tm.assert_series_equal(filled, expected)

filled = ser.fillna(method="bfill")
expected = Series([1.0, 1.0, 3.0, 3.0, np.nan], ser.index)
tm.assert_series_equal(filled, expected)
