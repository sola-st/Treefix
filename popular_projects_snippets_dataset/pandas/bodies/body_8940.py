# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
import scipy.sparse

sp_dtype = SparseDtype(dtype, np.array(0, dtype=dtype).item())

mat = scipy.sparse.eye(10, format=format, dtype=dtype)
result = pd.DataFrame.sparse.from_spmatrix(mat, index=labels, columns=labels)
expected = pd.DataFrame(
    np.eye(10, dtype=dtype), index=labels, columns=labels
).astype(sp_dtype)
tm.assert_frame_equal(result, expected)
