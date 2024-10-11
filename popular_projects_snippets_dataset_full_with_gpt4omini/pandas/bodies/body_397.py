# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
from scipy.sparse import bsr_matrix

assert com.is_scipy_sparse(bsr_matrix([1, 2, 3]))

assert not com.is_scipy_sparse(SparseArray([1, 2, 3]))
