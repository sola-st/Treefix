# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
df = DataFrame({"A": [1, 2]})
result = get_dummies(df, columns=["A"], sparse=True)
dtype = SparseDtype("bool", 0)
expected = DataFrame(
    {
        "A_1": SparseArray([1, 0], dtype=dtype),
        "A_2": SparseArray([0, 1], dtype=dtype),
    }
)
tm.assert_frame_equal(result, expected)
