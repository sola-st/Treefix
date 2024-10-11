# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
import scipy.sparse

row = [0, 3, 1, 0]
col = [0, 3, 1, 2]
data = [4, 5, 7, 9]
# TODO(scipy#13585): Remove dtype when scipy is fixed
# https://github.com/scipy/scipy/issues/13585
sp_array = scipy.sparse.coo_matrix((data, (row, col)), dtype="int")
result = pd.Series.sparse.from_coo(sp_array)

index = pd.MultiIndex.from_arrays(
    [
        np.array([0, 0, 1, 3], dtype=np.int32),
        np.array([0, 2, 1, 3], dtype=np.int32),
    ],
)
expected = pd.Series([4, 9, 7, 5], index=index, dtype="Sparse[int]")
tm.assert_series_equal(result, expected)
