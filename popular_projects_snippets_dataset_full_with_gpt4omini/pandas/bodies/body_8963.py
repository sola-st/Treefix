# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
data = np.arange(10).astype(float)
out = SparseArray(data).mean()
assert out == 4.5

data[5] = np.nan
out = SparseArray(data).mean()
assert out == 40.0 / 9
