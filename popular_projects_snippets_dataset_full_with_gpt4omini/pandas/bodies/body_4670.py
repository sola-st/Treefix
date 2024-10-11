# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
samples = np.hstack([samples, np.nan])
skew = nanops.nanskew(samples, skipna=True)
tm.assert_almost_equal(skew, actual_skew)
