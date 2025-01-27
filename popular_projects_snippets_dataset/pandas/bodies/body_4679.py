# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
samples = np.hstack([samples, np.nan])
kurt = nanops.nankurt(samples, skipna=True)
tm.assert_almost_equal(kurt, actual_kurt)
