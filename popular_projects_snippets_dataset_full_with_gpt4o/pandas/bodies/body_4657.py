# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
samples_test = np.nan * np.ones(2 * samples.shape[0])
samples_test[::2] = samples

actual_std = nanops.nanstd(samples_test, skipna=True)
tm.assert_almost_equal(actual_std, variance**0.5, rtol=1e-2)

actual_std = nanops.nanvar(samples_test, skipna=False)
tm.assert_almost_equal(actual_std, np.nan, rtol=1e-2)
