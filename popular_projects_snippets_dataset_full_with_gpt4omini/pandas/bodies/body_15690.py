# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_diff.py
# with tz
ser = Series(
    date_range("2000-01-01 09:00:00", periods=5, tz="US/Eastern"), name="foo"
)
result = ser.diff()
expected = Series(TimedeltaIndex(["NaT"] + ["1 days"] * 4), name="foo")
tm.assert_series_equal(result, expected)
