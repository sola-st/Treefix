# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 40652
result = DataFrame([[1, 2], [3, 4]]).applymap(lambda x, y: x + y, y=2)
expected = DataFrame([[3, 4], [5, 6]])
tm.assert_frame_equal(result, expected)
