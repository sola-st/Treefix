# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
rng = period_range("1/1/2000", freq="Q", periods=3)
tdi = TimedeltaIndex(["-1 Day", "-1 Day", "-1 Day"])
tdarr = tdi.values

msg = r"Cannot add or subtract timedelta64\[ns\] dtype from period\[Q-DEC\]"
with pytest.raises(TypeError, match=msg):
    rng + tdarr
with pytest.raises(TypeError, match=msg):
    tdarr + rng

with pytest.raises(TypeError, match=msg):
    rng - tdarr
msg = r"cannot subtract PeriodArray from TimedeltaArray"
with pytest.raises(TypeError, match=msg):
    tdarr - rng
