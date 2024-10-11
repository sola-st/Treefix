# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
prefixes = ["from_A", "from_B"]
result = get_dummies(df, prefix=prefixes, sparse=sparse)
expected = DataFrame(
    {
        "C": [1, 2, 3],
        "from_A_a": [True, False, True],
        "from_A_b": [False, True, False],
        "from_B_b": [True, True, False],
        "from_B_c": [False, False, True],
    },
)
expected[["C"]] = df[["C"]]
cols = ["from_A_a", "from_A_b", "from_B_b", "from_B_c"]
expected = expected[["C"] + cols]

typ = SparseArray if sparse else Series
expected[cols] = expected[cols].apply(lambda x: typ(x))
tm.assert_frame_equal(result, expected)
