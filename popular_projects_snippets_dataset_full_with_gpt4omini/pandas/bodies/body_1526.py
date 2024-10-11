# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
import scipy.sparse

spmatrix_t = getattr(scipy.sparse, spmatrix_t)

# The bug is triggered by a sparse matrix with purely sparse columns.  So the
# recipe below generates a rectangular matrix of dimension (5, 7) where all the
# diagonal cells are ones, meaning the last two columns are purely sparse.
rows, cols = 5, 7
spmatrix = spmatrix_t(np.eye(rows, cols, dtype=dtype), dtype=dtype)
df = DataFrame.sparse.from_spmatrix(spmatrix)

# regression test for GH#34526
itr_idx = range(2, rows)
result = df.loc[itr_idx].values
expected = spmatrix.toarray()[itr_idx]
tm.assert_numpy_array_equal(result, expected)

# regression test for GH#34540
result = df.loc[itr_idx].dtypes.values
expected = np.full(cols, SparseDtype(dtype, fill_value=0))
tm.assert_numpy_array_equal(result, expected)
