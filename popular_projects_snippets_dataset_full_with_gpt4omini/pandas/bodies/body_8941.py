# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
import scipy.sparse

mat = scipy.sparse.random(10, 2, density=0.5, format=format)
mat.data[0] = 0
result = pd.DataFrame.sparse.from_spmatrix(mat)
dtype = SparseDtype("float64", 0.0)
expected = pd.DataFrame(mat.todense()).astype(dtype)
tm.assert_frame_equal(result, expected)
