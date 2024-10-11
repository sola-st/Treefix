# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
index = IntIndex(10, [0, 1, 2, 3, 4])
assert index.equals(index)
assert not index.equals(IntIndex(10, [0, 1, 2, 3]))
