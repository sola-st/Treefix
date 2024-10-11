# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#18162
op = comparison_op

dr = date_range("2016-01-01", periods=6)
dz = dr.tz_localize("US/Pacific")

dr = tm.box_expected(dr, box_with_array)
dz = tm.box_expected(dz, box_with_array)

# Check comparisons against scalar Timestamps
ts = Timestamp("2000-03-14 01:59")
ts_tz = Timestamp("2000-03-14 01:59", tz="Europe/Amsterdam")

assert np.all(dr > ts)
msg = r"Invalid comparison between dtype=datetime64\[ns.*\] and Timestamp"
if op not in [operator.eq, operator.ne]:
    with pytest.raises(TypeError, match=msg):
        op(dr, ts_tz)

assert np.all(dz > ts_tz)
if op not in [operator.eq, operator.ne]:
    with pytest.raises(TypeError, match=msg):
        op(dz, ts)

if op not in [operator.eq, operator.ne]:
    # GH#12601: Check comparison against Timestamps and DatetimeIndex
    with pytest.raises(TypeError, match=msg):
        op(ts, dz)
