# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
# Check that arithmetic behavior matches non-Sparse Series arithmetic

if isinstance(a_dense, np.ndarray):
    expected = op(pd.Series(a_dense), b_dense).values
elif isinstance(b_dense, np.ndarray):
    expected = op(a_dense, pd.Series(b_dense)).values
else:
    raise NotImplementedError

with np.errstate(invalid="ignore", divide="ignore"):
    if mix:
        result = op(a, b_dense).to_dense()
    else:
        result = op(a, b).to_dense()

self._assert(result, expected)
