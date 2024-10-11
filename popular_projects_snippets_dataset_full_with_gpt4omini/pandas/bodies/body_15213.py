# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_mask.py
# dtype changes
ser = Series([1, 2, 3, 4])
result = ser.mask(ser > 2, np.nan)
expected = Series([1, 2, np.nan, np.nan])
tm.assert_series_equal(result, expected)
