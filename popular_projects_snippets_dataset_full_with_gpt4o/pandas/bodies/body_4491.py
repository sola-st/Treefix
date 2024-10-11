# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
cop = DataFrame(float_frame, copy=True)
cop["A"] = 5
assert (cop["A"] == 5).all()
assert not (float_frame["A"] == 5).all()
