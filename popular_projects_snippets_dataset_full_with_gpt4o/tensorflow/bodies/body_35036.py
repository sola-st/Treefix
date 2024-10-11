# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
batch_size = 6
a_p = np.array([0.5] * batch_size, dtype=np.float32)
b_p = np.array([0.4] * batch_size, dtype=np.float32)

a = bernoulli.Bernoulli(probs=a_p)
b = bernoulli.Bernoulli(probs=b_p)

kl = kullback_leibler.kl_divergence(a, b)
kl_val = self.evaluate(kl)

kl_expected = (a_p * np.log(a_p / b_p) + (1. - a_p) * np.log(
    (1. - a_p) / (1. - b_p)))

self.assertEqual(kl.get_shape(), (batch_size,))
self.assertAllClose(kl_val, kl_expected)
