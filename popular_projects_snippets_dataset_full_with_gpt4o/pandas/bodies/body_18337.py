# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#20049 subtracting PeriodIndex should raise TypeError
tdi = TimedeltaIndex(["1 hours", "2 hours"], freq=tdi_freq)
dti = Timestamp("2018-03-07 17:16:40") + tdi
pi = dti.to_period(pi_freq)
per = pi[0]

tdi = tm.box_expected(tdi, box_with_array)
pi = tm.box_expected(pi, box_with_array2)
msg = "cannot subtract|unsupported operand type"
with pytest.raises(TypeError, match=msg):
    tdi - pi

# GH#13078 subtraction of Period scalar not supported
with pytest.raises(TypeError, match=msg):
    tdi - per
