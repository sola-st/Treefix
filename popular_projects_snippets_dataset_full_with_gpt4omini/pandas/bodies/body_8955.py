# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
# GH#17570
out = SparseArray(data).all()
assert out

out = SparseArray(data, fill_value=pos).all()
assert out

data[1] = neg
out = SparseArray(data).all()
assert not out

out = SparseArray(data, fill_value=pos).all()
assert not out
