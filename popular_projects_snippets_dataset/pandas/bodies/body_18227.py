# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#1134
tm.assert_series_equal(first + second, expected)
tm.assert_series_equal(second + first, expected)
