# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
samples = np.vstack([samples, np.nan * np.ones(len(samples))])
kurt = nanops.nankurt(samples, axis=1)
tm.assert_almost_equal(kurt, np.array([actual_kurt, np.nan]))
