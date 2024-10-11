# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# These are normally union/diff set-like ops
tdi = TimedeltaIndex(["1 days", NaT, "2 days"], name="foo")
dti = pd.date_range("20130101", periods=3, name="bar")

result = tdi - tdi
expected = TimedeltaIndex(["0 days", NaT, "0 days"], name="foo")
tm.assert_index_equal(result, expected)

result = tdi + tdi
expected = TimedeltaIndex(["2 days", NaT, "4 days"], name="foo")
tm.assert_index_equal(result, expected)

result = dti - tdi  # name will be reset
expected = DatetimeIndex(["20121231", NaT, "20130101"])
tm.assert_index_equal(result, expected)
