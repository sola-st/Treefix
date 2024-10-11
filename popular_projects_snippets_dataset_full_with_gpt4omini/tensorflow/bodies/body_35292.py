# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
with self.cached_session():
    histograms = [[[0.2, 0.8], [0.4, 0.6]]]
    dist = categorical.Categorical(math_ops.log(histograms) - 50.)
    n = 10000
    samples = dist.sample(n, seed=123)
    samples.set_shape([n, 1, 2])
    self.assertEqual(samples.dtype, dtypes.int32)
    sample_values = self.evaluate(samples)
    self.assertFalse(np.any(sample_values < 0))
    self.assertFalse(np.any(sample_values > 1))
    self.assertAllClose(
        [[0.2, 0.4]], np.mean(
            sample_values == 0, axis=0), atol=1e-2)
    self.assertAllClose(
        [[0.8, 0.6]], np.mean(
            sample_values == 1, axis=0), atol=1e-2)
