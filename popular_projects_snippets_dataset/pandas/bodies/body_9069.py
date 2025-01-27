# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
import scipy.sparse

mat = scipy.sparse.random(10, 1, density=0.5, format=format)
mat.data[0] = 0
result = SparseArray.from_spmatrix(mat)

result = np.asarray(result)
expected = mat.toarray().ravel()
tm.assert_numpy_array_equal(result, expected)
