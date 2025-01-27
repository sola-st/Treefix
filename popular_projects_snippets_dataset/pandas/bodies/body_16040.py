# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_dropna.py
# GH#13737
ser = Series([Period("2011-01", freq="M"), Period("NaT", freq="M")])
result = ser.dropna()
expected = Series([Period("2011-01", freq="M")])

tm.assert_series_equal(result, expected)
