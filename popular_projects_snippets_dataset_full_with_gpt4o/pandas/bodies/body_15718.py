# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_duplicated.py
ser = Series([np.nan, 3, 3, None, np.nan], dtype=object)

result = ser.duplicated(keep=keep)
tm.assert_series_equal(result, expected)
