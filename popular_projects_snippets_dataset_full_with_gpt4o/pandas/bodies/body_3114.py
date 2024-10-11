# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
ps = tm.makePeriodFrame()
ps = tm.get_obj(ps, frame_or_series)
msg = "Given freq M does not match PeriodIndex freq B"
with pytest.raises(ValueError, match=msg):
    ps.shift(freq="M")
