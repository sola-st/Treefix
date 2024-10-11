# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH 5797
ser = pd.Series(pd.date_range("20130101", periods=5))
expected = ser.copy()
expected.loc[2] = pd.Timestamp("20120101")
result = ser.replace({pd.Timestamp("20130103"): pd.Timestamp("20120101")})
tm.assert_series_equal(result, expected)
result = ser.replace(pd.Timestamp("20130103"), pd.Timestamp("20120101"))
tm.assert_series_equal(result, expected)
