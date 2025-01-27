# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
empty_frame = DataFrame()

axis0 = empty_frame.sum(0)
axis1 = empty_frame.sum(1)
assert isinstance(axis0, Series)
assert isinstance(axis1, Series)
assert len(axis0) == 0
assert len(axis1) == 0
