# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#4532
# operate with pd.offsets
s = Series([Timestamp("20130101 9:01"), Timestamp("20130101 9:02")])

result = s + pd.offsets.Milli(5)
result2 = pd.offsets.Milli(5) + s
expected = Series(
    [Timestamp("20130101 9:01:00.005"), Timestamp("20130101 9:02:00.005")]
)
tm.assert_series_equal(result, expected)
tm.assert_series_equal(result2, expected)

result = s + pd.offsets.Minute(5) + pd.offsets.Milli(5)
expected = Series(
    [Timestamp("20130101 9:06:00.005"), Timestamp("20130101 9:07:00.005")]
)
tm.assert_series_equal(result, expected)
