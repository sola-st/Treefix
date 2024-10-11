# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
pi = period_range("2000", periods=4)
parr = tm.box_expected(pi, box_with_array)
assert_invalid_comparison(parr, other, box_with_array)
