# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
obj = Series([1, 2])
if frame_or_series is DataFrame:
    obj = obj.to_frame()

assert obj.flags is obj.flags
obj2 = obj.copy()
assert obj2.flags is not obj.flags
