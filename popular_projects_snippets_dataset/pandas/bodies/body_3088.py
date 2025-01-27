# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# GH#22397
if frame_or_series is not Series:
    obj = obj.to_frame()
assert obj.shift(shift_size) is not obj
