# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#40180
idx = index_or_series([0, 1, 2])
assert not np.all(idx)
assert np.any(idx)
idx = Index([1, 2, 3])
assert np.all(idx)
