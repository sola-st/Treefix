# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
a = constant_op.constant([3.0, 4.0])
b = constant_op.constant(13.0)
a1_v = 3.0
a2_v = 4.0
b_v = 13.0
n = constant_op.constant(100000)
uniform = uniform_lib.Uniform(low=a, high=b)

samples = uniform.sample(n, seed=137)
sample_values = self.evaluate(samples)
self.assertEqual(sample_values.shape, (100000, 2))
self.assertAllClose(
    sample_values[::, 0].mean(), (b_v + a1_v) / 2, atol=1e-1, rtol=0.)
self.assertAllClose(
    sample_values[::, 1].mean(), (b_v + a2_v) / 2, atol=1e-1, rtol=0.)
self.assertFalse(
    np.any(sample_values[::, 0] < a1_v) or np.any(sample_values >= b_v))
self.assertFalse(
    np.any(sample_values[::, 1] < a2_v) or np.any(sample_values >= b_v))
