# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# with datetimes/timedelta and tdi/dti
tdi = TimedeltaIndex(["1 days", NaT, "2 days"], name="foo")
dti = pd.date_range("20130101", periods=3, name="bar")
td = Timedelta("1 days")
dt = Timestamp("20130101")

msg = "cannot subtract a datelike from a TimedeltaArray"
with pytest.raises(TypeError, match=msg):
    tdi - dt
with pytest.raises(TypeError, match=msg):
    tdi - dti

msg = r"unsupported operand type\(s\) for -"
with pytest.raises(TypeError, match=msg):
    td - dt

msg = "(bad|unsupported) operand type for unary"
with pytest.raises(TypeError, match=msg):
    td - dti

result = dt - dti
expected = TimedeltaIndex(["0 days", "-1 days", "-2 days"], name="bar")
tm.assert_index_equal(result, expected)

result = dti - dt
expected = TimedeltaIndex(["0 days", "1 days", "2 days"], name="bar")
tm.assert_index_equal(result, expected)

result = tdi - td
expected = TimedeltaIndex(["0 days", NaT, "1 days"], name="foo")
tm.assert_index_equal(result, expected, check_names=False)

result = td - tdi
expected = TimedeltaIndex(["0 days", NaT, "-1 days"], name="foo")
tm.assert_index_equal(result, expected, check_names=False)

result = dti - td
expected = DatetimeIndex(
    ["20121231", "20130101", "20130102"], freq="D", name="bar"
)
tm.assert_index_equal(result, expected, check_names=False)

result = dt - tdi
expected = DatetimeIndex(["20121231", NaT, "20121230"], name="foo")
tm.assert_index_equal(result, expected)
