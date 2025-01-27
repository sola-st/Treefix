# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
result = get_dummies(df, sparse=sparse, dtype=dtype)
if sparse:
    arr = SparseArray
    typ = SparseDtype(dtype, 0)
else:
    arr = np.array
    typ = dtype
expected = DataFrame(
    {
        "C": [1, 2, 3],
        "A_a": arr([1, 0, 1], dtype=typ),
        "A_b": arr([0, 1, 0], dtype=typ),
        "B_b": arr([1, 1, 0], dtype=typ),
        "B_c": arr([0, 0, 1], dtype=typ),
    }
)
expected = expected[["C", "A_a", "A_b", "B_b", "B_c"]]
tm.assert_frame_equal(result, expected)
