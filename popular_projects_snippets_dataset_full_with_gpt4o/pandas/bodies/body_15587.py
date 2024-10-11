# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH#8209
ser = Series([np.nan, Timedelta("1 days")], index=["A", "B"])

result = ser.fillna(timedelta(1))
expected = Series(Timedelta("1 days"), index=["A", "B"])
tm.assert_series_equal(result, expected)
