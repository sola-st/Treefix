# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
# GH12402 Add a new parameter `drop_first` to avoid collinearity
# Basic case
s_list = list("abc")
s_series = Series(s_list)
s_series_index = Series(s_list, list("ABC"))

expected = DataFrame({"b": [0, 1, 0], "c": [0, 0, 1]}, dtype=bool)

result = get_dummies(s_list, drop_first=True, sparse=sparse)
if sparse:
    expected = expected.apply(SparseArray, fill_value=0)
tm.assert_frame_equal(result, expected)

result = get_dummies(s_series, drop_first=True, sparse=sparse)
tm.assert_frame_equal(result, expected)

expected.index = list("ABC")
result = get_dummies(s_series_index, drop_first=True, sparse=sparse)
tm.assert_frame_equal(result, expected)
