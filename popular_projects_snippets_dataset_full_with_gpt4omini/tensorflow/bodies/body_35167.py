# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a = [1., 2, 3]
b = [2., 4, 1.2]
dist = beta_lib.Beta(a, b)
self.assertEqual(dist.mean().get_shape(), (3,))
if not stats:
    exit()
expected_mean = stats.beta.mean(a, b)
self.assertAllClose(expected_mean, self.evaluate(dist.mean()))
