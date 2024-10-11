# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
data = DataFrame(
    {
        "A": [1, 2, 1],
        "B": Categorical(["a", "b", "a"]),
        "C": [1, 2, 1],
        "D": [1.0, 2.0, 1.0],
    }
)
columns = ["C", "D", "A_1", "A_2", "B_a", "B_b"]
expected = DataFrame(
    [[1, 1.0, 1, 0, 1, 0], [2, 2.0, 0, 1, 0, 1], [1, 1.0, 1, 0, 1, 0]],
    columns=columns,
)
expected[columns[2:]] = expected[columns[2:]].astype(dtype)
result = get_dummies(data, columns=["A", "B"], dtype=dtype)
tm.assert_frame_equal(result, expected)
