# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
dummies = DataFrame({"a": [1, 0, 0], "b": [0, 1, 0]})
result = from_dummies(dummies, default_category=default_category)
tm.assert_frame_equal(result, expected)
