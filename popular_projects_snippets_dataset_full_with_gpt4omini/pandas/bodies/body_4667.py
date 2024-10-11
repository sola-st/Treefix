# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
skew = nanops.nanskew(samples)
tm.assert_almost_equal(skew, actual_skew)
