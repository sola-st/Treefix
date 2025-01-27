# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
samples_test = np.nan * np.ones(2 * samples.shape[0])
samples_test[::2] = samples

actual_variance = nanops.nanvar(samples_test, skipna=True)
tm.assert_almost_equal(actual_variance, variance, rtol=1e-2)

actual_variance = nanops.nanvar(samples_test, skipna=False)
tm.assert_almost_equal(actual_variance, np.nan, rtol=1e-2)
