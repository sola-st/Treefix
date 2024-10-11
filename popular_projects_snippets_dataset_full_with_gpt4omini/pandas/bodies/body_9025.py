# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
index = BlockIndex(10, [0, 4], [2, 5])

assert index.equals(index)
assert not index.equals(BlockIndex(10, [0, 4], [2, 6]))
