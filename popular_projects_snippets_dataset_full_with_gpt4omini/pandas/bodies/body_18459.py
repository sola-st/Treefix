# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#12534, fixed by GH#19024
dt = Timestamp("1700-01-31")
td = Timedelta("20000 Days")
dti = date_range("1949-09-30", freq="100Y", periods=4)
ser = Series(dti)
msg = "Overflow in int64 addition"
with pytest.raises(OverflowError, match=msg):
    ser - dt
with pytest.raises(OverflowError, match=msg):
    dt - ser
with pytest.raises(OverflowError, match=msg):
    ser + td
with pytest.raises(OverflowError, match=msg):
    td + ser

ser.iloc[-1] = NaT
expected = Series(
    ["2004-10-03", "2104-10-04", "2204-10-04", "NaT"], dtype="datetime64[ns]"
)
res = ser + td
tm.assert_series_equal(res, expected)
res = td + ser
tm.assert_series_equal(res, expected)

ser.iloc[1:] = NaT
expected = Series(["91279 Days", "NaT", "NaT", "NaT"], dtype="timedelta64[ns]")
res = ser - dt
tm.assert_series_equal(res, expected)
res = dt - ser
tm.assert_series_equal(res, -expected)
