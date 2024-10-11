# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
data = np.arange(10).astype(float)
out = SparseArray(data).sum()
assert out == 45.0

data[5] = np.nan
out = SparseArray(data, fill_value=2).sum()
assert out == 40.0

out = SparseArray(data, fill_value=np.nan).sum()
assert out == 40.0
