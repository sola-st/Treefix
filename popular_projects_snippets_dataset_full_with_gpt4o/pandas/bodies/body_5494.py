# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
# GH#36131 comparing Timestamp with date object is deprecated
ts = Timestamp("2021-01-01 00:00:00.00000", tz=tz)
dt = ts.to_pydatetime().date()
# in 2.0 we disallow comparing pydate objects with Timestamps,
#  following the stdlib datetime behavior.

msg = "Cannot compare Timestamp with datetime.date"
for left, right in [(ts, dt), (dt, ts)]:
    assert not left == right
    assert left != right

    with pytest.raises(TypeError, match=msg):
        left < right
    with pytest.raises(TypeError, match=msg):
        left <= right
    with pytest.raises(TypeError, match=msg):
        left > right
    with pytest.raises(TypeError, match=msg):
        left >= right
