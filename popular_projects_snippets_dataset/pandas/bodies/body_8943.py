# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
import scipy.sparse

df = pd.DataFrame(
    {colnames[0]: [0, 1, 0], colnames[1]: [1, 0, 0]}, dtype="Sparse[int64, 0]"
)
result = df.sparse.to_coo()
expected = scipy.sparse.coo_matrix(np.asarray(df))
assert (result != expected).nnz == 0
