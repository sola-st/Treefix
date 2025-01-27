# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
dummies = DataFrame(
    {"a": [1, 0, 0, 1], "b": [False, True, False, False], "c": [0, 0, 1, 0]}
)
expected = DataFrame({"": ["a", "b", "c", "a"]})
result = from_dummies(dummies)
tm.assert_frame_equal(result, expected)
