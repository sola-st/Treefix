# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# shift by 0
obj = tm.get_obj(datetime_frame, frame_or_series)
unshifted = obj.shift(0)
tm.assert_equal(unshifted, obj)
