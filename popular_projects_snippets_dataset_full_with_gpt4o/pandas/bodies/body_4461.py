# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# Issue 25075
data = [[1, 2], (3, 4)]
result = DataFrame(data)
expected = DataFrame([[1, 2], [3, 4]])
tm.assert_frame_equal(result, expected)
