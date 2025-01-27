# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isna.py
# GH#13737
ser = Series([Period("2011-01", freq="M"), Period("NaT", freq="M")])

expected = Series([False, True])

result = ser.isna()
tm.assert_series_equal(result, expected)

result = ser.notna()
tm.assert_series_equal(result, ~expected)
