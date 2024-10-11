# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
result = get_dummies(df, prefix=["from_A"], columns=["A"], sparse=sparse)
expected = DataFrame(
    {
        "B": ["b", "b", "c"],
        "C": [1, 2, 3],
        "from_A_a": [1, 0, 1],
        "from_A_b": [0, 1, 0],
    },
)
cols = expected.columns
expected[cols[1:]] = expected[cols[1:]].astype(bool)
expected[["C"]] = df[["C"]]
if sparse:
    cols = ["from_A_a", "from_A_b"]
    expected[cols] = expected[cols].astype(SparseDtype("bool", 0))
tm.assert_frame_equal(result, expected)
