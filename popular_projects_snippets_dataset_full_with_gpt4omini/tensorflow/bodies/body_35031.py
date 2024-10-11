# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
p = [0.2, 0.6]
dist = bernoulli.Bernoulli(probs=p)
n = 100000
samples = dist.sample(n)
samples.set_shape([n, 2])
self.assertEqual(samples.dtype, dtypes.int32)
sample_values = self.evaluate(samples)
self.assertTrue(np.all(sample_values >= 0))
self.assertTrue(np.all(sample_values <= 1))
# Note that the standard error for the sample mean is ~ sqrt(p * (1 - p) /
# n). This means that the tolerance is very sensitive to the value of p
# as well as n.
self.assertAllClose(p, np.mean(sample_values, axis=0), atol=1e-2)
self.assertEqual(set([0, 1]), set(sample_values.flatten()))
# In this test we're just interested in verifying there isn't a crash
# owing to mismatched types. b/30940152
dist = bernoulli.Bernoulli(np.log([.2, .4]))
self.assertAllEqual((1, 2), dist.sample(1, seed=42).get_shape().as_list())
