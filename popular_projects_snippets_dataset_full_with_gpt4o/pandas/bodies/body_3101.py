# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
obj = datetime_frame.T
offset = offsets.BDay()

# GH#47039
shifted = obj.shift(5, freq=offset, axis=1)
assert len(shifted) == len(obj)
unshifted = shifted.shift(-5, freq=offset, axis=1)
tm.assert_equal(unshifted, obj)
