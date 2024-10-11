# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
# GH8846
# size property should be defined

o = construct(frame_or_series, shape=10)
assert o.size == np.prod(o.shape)
assert o.size == 10 ** len(o.axes)
