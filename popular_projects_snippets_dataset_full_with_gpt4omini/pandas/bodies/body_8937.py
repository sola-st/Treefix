# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
import scipy.sparse

values = SparseArray([0, np.nan, 1, 0, None, 3], fill_value=0)
index = pd.MultiIndex.from_tuples(
    [
        ("b", 2, "z", 1),
        ("a", 2, "z", 2),
        ("a", 2, "z", 1),
        ("a", 2, "x", 2),
        ("b", 1, "z", 1),
        ("a", 1, "z", 0),
    ]
)
ss = pd.Series(values, index=index)

expected_A = np.zeros((4, 4))
for value, (row, col) in expected_values_pos.items():
    expected_A[row, col] = value

A, rows, cols = ss.sparse.to_coo(
    row_levels=(0, 1), column_levels=(2, 3), sort_labels=sort_labels
)
assert isinstance(A, scipy.sparse.coo_matrix)
tm.assert_numpy_array_equal(A.toarray(), expected_A)
assert rows == expected_rows
assert cols == expected_cols
