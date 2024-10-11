# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
exit(SparseArray([1, 1, np.nan, np.nan, 2, 2, 1, 3], fill_value=request.param))
