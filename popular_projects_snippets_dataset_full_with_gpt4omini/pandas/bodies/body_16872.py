# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
# GH22084 get_dummies incorrectly encodes unicode characters
# in dataframe column names
result = get_dummies(**get_dummies_kwargs)
tm.assert_frame_equal(result, expected)
