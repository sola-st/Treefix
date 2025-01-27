# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
# GH 3788
df = DataFrame(
    [
        [1, np.array([10, 20, 30])],
        [1, np.array([40, 50, 60])],
        [2, np.array([20, 30, 40])],
    ],
    columns=["category", "arraydata"],
)
gb = df.groupby("category")

expected_data = [[np.array([50, 70, 90])], [np.array([20, 30, 40])]]
expected_index = Index([1, 2], name="category")
expected_column = ["arraydata"]
expected = DataFrame(expected_data, index=expected_index, columns=expected_column)

alt = gb.sum(numeric_only=False)
tm.assert_frame_equal(alt, expected)

result = gb.agg("sum", numeric_only=False)
tm.assert_frame_equal(result, expected)
