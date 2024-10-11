# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#1134
tm.assert_frame_equal(first + second, expected)
tm.assert_frame_equal(second + first, expected)
