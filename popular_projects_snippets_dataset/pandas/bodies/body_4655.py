# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
actual_variance = nanops.nanvar(samples)
tm.assert_almost_equal(actual_variance, variance, rtol=1e-2)
