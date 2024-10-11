# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
dummies = DataFrame(
    {
        "a": [True, False, False, True],
        "b": [False, True, False, False],
        "c": [False, False, True, False],
    }
)
expected = DataFrame({"": ["a", "b", "c", "a"]})
result = from_dummies(dummies)
tm.assert_frame_equal(result, expected)
