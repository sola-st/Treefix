# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
result = DataFrame({"A": [(1, 2), (3, 4)]})
expected = DataFrame({"A": Series([(1, 2), (3, 4)])})
tm.assert_frame_equal(result, expected)
