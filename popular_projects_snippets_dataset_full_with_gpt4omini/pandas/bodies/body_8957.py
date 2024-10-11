# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
# GH#17570
out = SparseArray(data).any()
assert out

out = SparseArray(data, fill_value=pos).any()
assert out

data[1] = neg
out = SparseArray(data).any()
assert not out

out = SparseArray(data, fill_value=pos).any()
assert not out
