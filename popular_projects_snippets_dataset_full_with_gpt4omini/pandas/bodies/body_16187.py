# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH#45810
ser1 = Series([0, np.nan], dtype="float")
ser2 = Series([0, 1], dtype="Int64")
result = ser1 * ser2
expected = Series([0, pd.NA], dtype="Float64")
tm.assert_series_equal(result, expected)
