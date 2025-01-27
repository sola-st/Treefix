# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
# DISABLED: Please enable this test once b/issues/30149644 is resolved.
batch_size = 2
a_v = [3.0, 22.0]
b_v = [13.0, 35.0]
a = constant_op.constant([a_v] * batch_size)
b = constant_op.constant([b_v] * batch_size)

uniform = uniform_lib.Uniform(low=a, high=b)

n_v = 100000
n = constant_op.constant(n_v)
samples = uniform.sample(n)
self.assertEqual(samples.get_shape(), (n_v, batch_size, 2))

sample_values = self.evaluate(samples)

self.assertFalse(
    np.any(sample_values[:, 0, 0] < a_v[0]) or
    np.any(sample_values[:, 0, 0] >= b_v[0]))
self.assertFalse(
    np.any(sample_values[:, 0, 1] < a_v[1]) or
    np.any(sample_values[:, 0, 1] >= b_v[1]))

self.assertAllClose(
    sample_values[:, 0, 0].mean(), (a_v[0] + b_v[0]) / 2, atol=1e-2)
self.assertAllClose(
    sample_values[:, 0, 1].mean(), (a_v[1] + b_v[1]) / 2, atol=1e-2)
