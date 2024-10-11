# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
df["cat"] = Categorical(["x", "y", "y"])
result = get_dummies(df, drop_first=True, sparse=sparse)
expected = DataFrame(
    {"C": [1, 2, 3], "A_b": [0, 1, 0], "B_c": [0, 0, 1], "cat_y": [0, 1, 1]}
)
cols = ["A_b", "B_c", "cat_y"]
expected[cols] = expected[cols].astype(bool)
expected = expected[["C", "A_b", "B_c", "cat_y"]]
if sparse:
    for col in cols:
        expected[col] = SparseArray(expected[col])
tm.assert_frame_equal(result, expected)
