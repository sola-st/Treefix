# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#17901
df = DataFrame({"A": [1, 1], "B": [1, 1]})
expected = DataFrame({"A": [2, 2], "B": [3, 3]})
result = df + values
tm.assert_frame_equal(result, expected)
