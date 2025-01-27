# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_interpolate.py
# GH#27628 missing.interpolate_2d should handle datetimetz values
dti = date_range("2015-04-05", periods=3, tz="US/Central")
ser = Series(dti)
ser[1] = pd.NaT
result = ser.interpolate(method="pad")

expected = Series(dti)
expected[1] = expected[0]
tm.assert_series_equal(result, expected)
