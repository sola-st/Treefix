# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a = np.random.rand(3, 2, 2).astype(np.float32)
b = np.random.rand(3, 2, 2).astype(np.float32)
beta = beta_lib.Beta(a, b)
n = constant_op.constant(100000)
samples = beta.sample(n)
sample_values = self.evaluate(samples)
self.assertEqual(sample_values.shape, (100000, 3, 2, 2))
self.assertFalse(np.any(sample_values < 0.0))
if not stats:
    exit()
self.assertAllClose(
    sample_values[:, 1, :].mean(axis=0),
    stats.beta.mean(a, b)[1, :],
    atol=1e-1)
