# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
# GH 15444
obj = construct(frame_or_series, shape)
obj_copy = func(obj)
assert obj_copy is not obj
tm.assert_equal(obj_copy, obj)
