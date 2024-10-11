# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
categories = DataFrame({"": ["a", "b", "c", "a"]})
dummies = get_dummies(categories)
result = from_dummies(dummies, sep="_")
expected = categories
tm.assert_frame_equal(result, expected)
