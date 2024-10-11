# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
dummies = DataFrame(
    {1: [1, 0, 0, 0], 25: [0, 1, 0, 0], 2: [0, 0, 1, 0], 5: [0, 0, 0, 1]}
)
expected = DataFrame({"": [1, 25, 2, 5]}, dtype="object")
result = from_dummies(dummies)
tm.assert_frame_equal(result, expected)
