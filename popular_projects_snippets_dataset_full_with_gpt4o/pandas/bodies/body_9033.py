# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
index = IntIndex(10, [2, 3, 4, 5, 6])
assert index.to_int_index() is index
