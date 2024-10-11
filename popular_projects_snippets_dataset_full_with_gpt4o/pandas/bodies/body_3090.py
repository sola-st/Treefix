# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
ts = tm.get_obj(datetime_frame, frame_or_series).astype(int)
shifted = ts.shift(1)
expected = ts.astype(float).shift(1)
tm.assert_equal(shifted, expected)
