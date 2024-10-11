# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_from_dummies.py
result = from_dummies(
    dummies_with_unassigned, sep="_", default_category=default_category
)
tm.assert_frame_equal(result, expected)
