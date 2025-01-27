# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
# Test the case that categorical variable only has one level.
s_list = list("aaa")
s_series = Series(s_list)
s_series_index = Series(s_list, list("ABC"))

expected = DataFrame(index=RangeIndex(3))

result = get_dummies(s_list, drop_first=True, sparse=sparse)
tm.assert_frame_equal(result, expected)

result = get_dummies(s_series, drop_first=True, sparse=sparse)
tm.assert_frame_equal(result, expected)

expected = DataFrame(index=list("ABC"))
result = get_dummies(s_series_index, drop_first=True, sparse=sparse)
tm.assert_frame_equal(result, expected)
