# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
# GH44965
df = df[["A", "B"]]
df = df.astype({"A": "object", "B": "string"})
result = get_dummies(df)
expected = DataFrame(
    {
        "A_a": [1, 0, 1],
        "A_b": [0, 1, 0],
        "B_b": [1, 1, 0],
        "B_c": [0, 0, 1],
    },
    dtype=bool,
)
tm.assert_frame_equal(result, expected)
