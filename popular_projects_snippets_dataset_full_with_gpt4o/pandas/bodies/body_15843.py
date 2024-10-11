# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
ser = pd.Series([np.nan, 0, np.inf])
tm.assert_series_equal(ser.replace(np.nan, 0), ser.fillna(0))

ser = pd.Series([np.nan, 0, "foo", "bar", np.inf, None, pd.NaT])
tm.assert_series_equal(ser.replace(np.nan, 0), ser.fillna(0))
filled = ser.copy()
filled[4] = 0
tm.assert_series_equal(ser.replace(np.inf, 0), filled)
