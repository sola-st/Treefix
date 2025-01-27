# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
ps = tm.makePeriodFrame()
ps = tm.get_obj(ps, frame_or_series)

shifted = ps.shift(1, freq="infer")
unshifted = shifted.shift(-1, freq="infer")
tm.assert_equal(unshifted, ps)

shifted2 = ps.shift(freq="B")
tm.assert_equal(shifted, shifted2)

shifted3 = ps.shift(freq=offsets.BDay())
tm.assert_equal(shifted, shifted3)
