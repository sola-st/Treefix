# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
df = pd.DataFrame(
    {
        "A": SparseArray([1, 0], dtype=SparseDtype("int64", 0)),
        "B": SparseArray([1, 0], dtype=SparseDtype("int64", 1)),
        "C": SparseArray([1.0, 0.0], dtype=SparseDtype("float64", 0.0)),
    },
    index=["b", "a"],
)
result = df.sparse.to_dense()
expected = pd.DataFrame(
    {"A": [1, 0], "B": [1, 0], "C": [1.0, 0.0]}, index=["b", "a"]
)
tm.assert_frame_equal(result, expected)
