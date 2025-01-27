# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py

left = DataFrame({"A": ["a", "b", "c"], "B": [1, 2, 3]})

result = left + left
expected = DataFrame({"A": ["aa", "bb", "cc"], "B": [2, 4, 6]})
tm.assert_frame_equal(result, expected)
