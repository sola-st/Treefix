# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# PeriodIndex + Timedelta-like is allowed only with
#   tick-like frequencies
rng = period_range("1/1/2000", freq="90D", periods=3)
tdi = TimedeltaIndex(["-1 Day", "-1 Day", "-1 Day"])
tdarr = tdi.values

expected = period_range("12/31/1999", freq="90D", periods=3)
result = rng + tdi
tm.assert_index_equal(result, expected)
result = rng + tdarr
tm.assert_index_equal(result, expected)
result = tdi + rng
tm.assert_index_equal(result, expected)
result = tdarr + rng
tm.assert_index_equal(result, expected)

expected = period_range("1/2/2000", freq="90D", periods=3)

result = rng - tdi
tm.assert_index_equal(result, expected)
result = rng - tdarr
tm.assert_index_equal(result, expected)

msg = r"cannot subtract .* from .*"
with pytest.raises(TypeError, match=msg):
    tdarr - rng

with pytest.raises(TypeError, match=msg):
    tdi - rng
