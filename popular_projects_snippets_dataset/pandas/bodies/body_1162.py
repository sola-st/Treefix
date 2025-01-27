# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_multiindex.py
# GH 38439
mi1 = MultiIndex.from_arrays([[81.0, np.nan], [np.nan, np.nan]])
mi2 = MultiIndex.from_arrays([[np.nan, 82.0], [np.nan, np.nan]])
ser1 = Series([1, 2], index=mi1)
ser2 = Series([1, 2], index=mi2)
result1, result2 = ser1.align(ser2)

mi = MultiIndex.from_arrays([[81.0, 82.0, np.nan], [np.nan, np.nan, np.nan]])
expected1 = Series([1.0, np.nan, 2.0], index=mi)
expected2 = Series([np.nan, 2.0, 1.0], index=mi)

tm.assert_series_equal(result1, expected1)
tm.assert_series_equal(result2, expected2)
