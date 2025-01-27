# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_copy.py
# don't want to be able to modify the index stored elsewhere after
# making a copy
ind = getattr(float_frame, attr)
ind.name = None
cp = float_frame.copy()
getattr(cp, attr).name = "foo"
assert getattr(float_frame, attr).name is None
