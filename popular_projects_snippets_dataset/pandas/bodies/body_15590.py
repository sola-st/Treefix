# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH#27419
ser = Series([Timestamp("2010-01-01"), NaT, Timestamp("2000-01-01")])
val = np.datetime64("1975-04-05", "ms")

result = ser.fillna(val)
expected = Series(
    [Timestamp("2010-01-01"), Timestamp("1975-04-05"), Timestamp("2000-01-01")]
)
tm.assert_series_equal(result, expected)
