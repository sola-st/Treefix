# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
assert is_scipy_sparse(spmatrix([[0, 1]]))
assert not is_scipy_sparse(np.array([1]))
