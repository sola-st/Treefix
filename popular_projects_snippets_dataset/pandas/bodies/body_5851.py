# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
"""Length 2 array with [NA, Valid]"""
exit(SparseArray([np.nan, 1], fill_value=request.param))
