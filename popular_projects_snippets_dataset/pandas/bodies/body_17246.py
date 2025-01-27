# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
dummies = DataFrame(
    {
        "col1_a": [1, 0, 0],
        "col1_b": [0, 1, 0],
        "col1_NaN": [0, 0, 1],
        "col2_a": [0, 1, 0],
        "col2_b": [0, 0, 0],
        "col2_c": [0, 0, 1],
        "col2_NaN": [1, 0, 0],
    },
)
expected = DataFrame({"col1": ["a", "b", "NaN"], "col2": ["NaN", "a", "c"]})
result = from_dummies(dummies, sep="_")
tm.assert_frame_equal(result, expected)
