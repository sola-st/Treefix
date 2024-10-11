# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
import scipy.sparse

A = scipy.sparse.eye(3, format="coo", dtype=dtype)
result = pd.Series.sparse.from_coo(A, dense_index=dense_index)

# TODO: GH49560: scipy.sparse.eye always has A.row and A.col dtype as int32.
# fix index_dtype to follow scipy.sparse convention (always int32)?
index_dtype = np.int64 if dense_index else np.int32
index = pd.MultiIndex.from_tuples(
    [
        np.array([0, 0], dtype=index_dtype),
        np.array([1, 1], dtype=index_dtype),
        np.array([2, 2], dtype=index_dtype),
    ],
)
expected = pd.Series(SparseArray(np.array([1, 1, 1], dtype=dtype)), index=index)
if dense_index:
    expected = expected.reindex(pd.MultiIndex.from_product(index.levels))

tm.assert_series_equal(result, expected)
