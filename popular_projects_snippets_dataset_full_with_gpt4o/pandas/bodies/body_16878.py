# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
df.loc[3, :] = [np.nan, np.nan, np.nan]
result = get_dummies(
    df, dummy_na=True, drop_first=True, sparse=sparse
).sort_index(axis=1)
expected = DataFrame(
    {
        "C": [1, 2, 3, np.nan],
        "A_b": [0, 1, 0, 0],
        "A_nan": [0, 0, 0, 1],
        "B_c": [0, 0, 1, 0],
        "B_nan": [0, 0, 0, 1],
    }
)
cols = ["A_b", "A_nan", "B_c", "B_nan"]
expected[cols] = expected[cols].astype(bool)
expected = expected.sort_index(axis=1)
if sparse:
    for col in cols:
        expected[col] = SparseArray(expected[col])

tm.assert_frame_equal(result, expected)

result = get_dummies(df, dummy_na=False, drop_first=True, sparse=sparse)
expected = expected[["C", "A_b", "B_c"]]
tm.assert_frame_equal(result, expected)
