# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
expected = DataFrame({"col1": ["a", "b", "a"], "col2": ["b", "a", "c"]})
result = from_dummies(dummies_basic, sep="_")
tm.assert_frame_equal(result, expected)
