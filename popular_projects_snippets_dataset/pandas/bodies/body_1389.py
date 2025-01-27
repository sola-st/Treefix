# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#22046
ser1 = Series([1, 2, 3])
ser2 = Series([4, 5, 6], index=[1, 0, 2])
ser1.iloc[1:3] = ser2.iloc[1:3]
expected = Series([1, 5, 6])
tm.assert_series_equal(ser1, expected)
