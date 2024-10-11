# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index([1, 2, 3, "a", "b", "c"])

assert index[1:3].identical(Index([2, 3], dtype=np.object_))
assert index[[0, 1]].identical(Index([1, 2], dtype=np.object_))
