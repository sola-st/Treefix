# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
# GH20839
df.columns = ["A", "A", "A"]
result = get_dummies(df).sort_index(axis=1)

expected = DataFrame(
    [
        [1, True, False, True, False],
        [2, False, True, True, False],
        [3, True, False, False, True],
    ],
    columns=["A", "A_a", "A_b", "A_b", "A_c"],
).sort_index(axis=1)

expected = expected.astype({"A": np.int64})

tm.assert_frame_equal(result, expected)
