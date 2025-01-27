# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
# Generate some sample data.
samples_unif = self.prng.uniform(size=samples.shape[0])
samples = np.vstack([samples, samples_unif])

actual_variance = nanops.nanvar(samples, axis=1)
tm.assert_almost_equal(
    actual_variance, np.array([variance, 1.0 / 12]), rtol=1e-2
)
