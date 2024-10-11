# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
samples = np.vstack([samples, np.nan * np.ones(len(samples))])
skew = nanops.nanskew(samples, axis=1)
tm.assert_almost_equal(skew, np.array([actual_skew, np.nan]))
