# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH#42630
ser1 = Series([15, pd.NA, 5, 4], dtype="Int64")
ser2 = Series([15, 5, np.nan, 4])
result = ser1 / ser2
expected = Series([1.0, pd.NA, pd.NA, 1.0], dtype="Float64")
tm.assert_series_equal(result, expected)

result = ser2 / ser1
tm.assert_series_equal(result, expected)
