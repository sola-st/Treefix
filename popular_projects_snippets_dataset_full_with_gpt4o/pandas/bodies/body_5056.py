# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_interval.py
# GH 18538
left = Timestamp("2017-01-01", tz=tz_left)
right = Timestamp("2017-01-02", tz=tz_right)

if com.any_none(tz_left, tz_right):
    error = TypeError
    msg = "Cannot compare tz-naive and tz-aware timestamps"
else:
    error = ValueError
    msg = "left and right must have the same time zone"
with pytest.raises(error, match=msg):
    Interval(left, right)
