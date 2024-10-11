# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_clip.py
median = float_frame.median().median()
original = float_frame.copy()

double = float_frame.clip(upper=median, lower=median)
assert not (double.values != median).any()

# Verify that float_frame was not changed inplace
assert (float_frame.values == original.values).all()
