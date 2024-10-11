# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
df.loc[3, :] = [np.nan, np.nan, np.nan]
result = get_dummies(df, dummy_na=True, sparse=sparse, dtype=dtype).sort_index(
    axis=1
)

if sparse:
    arr = SparseArray
    typ = SparseDtype(dtype, 0)
else:
    arr = np.array
    typ = dtype

expected = DataFrame(
    {
        "C": [1, 2, 3, np.nan],
        "A_a": arr([1, 0, 1, 0], dtype=typ),
        "A_b": arr([0, 1, 0, 0], dtype=typ),
        "A_nan": arr([0, 0, 0, 1], dtype=typ),
        "B_b": arr([1, 1, 0, 0], dtype=typ),
        "B_c": arr([0, 0, 1, 0], dtype=typ),
        "B_nan": arr([0, 0, 0, 1], dtype=typ),
    }
).sort_index(axis=1)

tm.assert_frame_equal(result, expected)

result = get_dummies(df, dummy_na=False, sparse=sparse, dtype=dtype)
expected = expected[["C", "A_a", "A_b", "B_b", "B_c"]]
tm.assert_frame_equal(result, expected)
