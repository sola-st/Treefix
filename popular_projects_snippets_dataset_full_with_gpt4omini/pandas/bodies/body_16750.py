# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# issue: 24782
a = DataFrame({col1: [1, 2, 3]})
b = DataFrame({col2: [4, 5, 6]})

expected = DataFrame([[1, 4], [2, 5], [3, 6]], columns=expected_cols)

result = a.merge(b, left_index=True, right_index=True, **kwargs)
tm.assert_frame_equal(result, expected)

result = merge(a, b, left_index=True, right_index=True, **kwargs)
tm.assert_frame_equal(result, expected)
