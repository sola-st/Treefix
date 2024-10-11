# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# API change from 0.12?
# GH 5319
ser = pd.Series([0, np.nan, 2, 3, 4])
expected = ser.ffill()
result = ser.replace([np.nan])
tm.assert_series_equal(result, expected)

ser = pd.Series([0, np.nan, 2, 3, 4])
expected = ser.ffill()
result = ser.replace(np.nan)
tm.assert_series_equal(result, expected)
