# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
# xref GH8846
o = construct(frame_or_series, shape=10)
assert len(np.array_split(o, 5)) == 5
assert len(np.array_split(o, 2)) == 2
