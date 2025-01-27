# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
import scipy.sparse

dtype = SparseDtype("float64", 0.0)

mat = scipy.sparse.random(10, 2, density=0.5)
result = pd.DataFrame.sparse.from_spmatrix(mat, columns=columns)
expected = pd.DataFrame(mat.toarray(), columns=columns).astype(dtype)
tm.assert_frame_equal(result, expected)
