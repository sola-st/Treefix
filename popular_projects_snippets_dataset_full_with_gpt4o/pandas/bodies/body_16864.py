# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
# not that you should do this...
result = get_dummies(df, prefix="bad", sparse=sparse)
bad_columns = ["bad_a", "bad_b", "bad_b", "bad_c"]
expected = DataFrame(
    [
        [1, True, False, True, False],
        [2, False, True, True, False],
        [3, True, False, False, True],
    ],
    columns=["C"] + bad_columns,
)
expected = expected.astype({"C": np.int64})
if sparse:
    # work around astyping & assigning with duplicate columns
    # https://github.com/pandas-dev/pandas/issues/14427
    expected = pd.concat(
        [
            Series([1, 2, 3], name="C"),
            Series([True, False, True], name="bad_a", dtype="Sparse[bool]"),
            Series([False, True, False], name="bad_b", dtype="Sparse[bool]"),
            Series([True, True, False], name="bad_b", dtype="Sparse[bool]"),
            Series([False, False, True], name="bad_c", dtype="Sparse[bool]"),
        ],
        axis=1,
    )

tm.assert_frame_equal(result, expected)
