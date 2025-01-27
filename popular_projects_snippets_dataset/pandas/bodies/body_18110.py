# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#28980
# comparison with scalar that cannot be interpreted as a Period
pi = period_range("2000", periods=4)
parr = tm.box_expected(pi, box_with_array)
assert_invalid_comparison(parr, scalar, box_with_array)
