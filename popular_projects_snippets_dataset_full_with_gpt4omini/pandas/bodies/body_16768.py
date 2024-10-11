# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH#22818
# Do not raise warning when duplicates are caused by duplicates in origin
left = DataFrame([[1, 1, 1], [2, 2, 2]], columns=["a", "b", "b"])
right = DataFrame({"a": [1, 3], "b": 2})
result = merge(left, right, on="a")
expected = DataFrame([[1, 1, 1, 2]], columns=["a", "b_x", "b_x", "b_y"])
tm.assert_frame_equal(result, expected)
