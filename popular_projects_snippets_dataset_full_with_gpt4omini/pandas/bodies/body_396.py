# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert com.is_sparse(SparseArray([1, 2, 3]))

assert not com.is_sparse(np.array([1, 2, 3]))

if check_scipy:
    import scipy.sparse

    assert not com.is_sparse(scipy.sparse.bsr_matrix([1, 2, 3]))
