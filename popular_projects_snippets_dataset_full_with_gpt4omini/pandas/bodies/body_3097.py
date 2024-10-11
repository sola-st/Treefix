# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# shift by DateOffset
obj = tm.get_obj(datetime_frame, frame_or_series)
offset = offsets.BDay()

shifted = obj.shift(5, freq=offset)
assert len(shifted) == len(obj)
unshifted = shifted.shift(-5, freq=offset)
tm.assert_equal(unshifted, obj)

shifted2 = obj.shift(5, freq="B")
tm.assert_equal(shifted, shifted2)

unshifted = obj.shift(0, freq=offset)
tm.assert_equal(unshifted, obj)

d = obj.index[0]
shifted_d = d + offset * 5
if frame_or_series is DataFrame:
    tm.assert_series_equal(obj.xs(d), shifted.xs(shifted_d), check_names=False)
else:
    tm.assert_almost_equal(obj.at[d], shifted.at[shifted_d])
