# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
# GH 21126
out = SparseArray(data, dtype=dtype)
assert out.shape == shape
