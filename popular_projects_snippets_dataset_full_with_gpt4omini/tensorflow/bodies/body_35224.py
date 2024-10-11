# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
conc1 = np.array([[1., 2., 3., 1.5, 2.5, 3.5],
                  [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]])
conc2 = np.array([[0.5, 1., 1.5, 2., 2.5, 3.]])

d1 = dirichlet_lib.Dirichlet(conc1)
d2 = dirichlet_lib.Dirichlet(conc2)
x = d1.sample(int(1e4), seed=0)
kl_sample = math_ops.reduce_mean(d1.log_prob(x) - d2.log_prob(x), 0)
kl_actual = kullback_leibler.kl_divergence(d1, d2)

kl_sample_val = self.evaluate(kl_sample)
kl_actual_val = self.evaluate(kl_actual)

self.assertEqual(conc1.shape[:-1], kl_actual.get_shape())

if not special:
    exit()

kl_expected = (
    special.gammaln(np.sum(conc1, -1))
    - special.gammaln(np.sum(conc2, -1))
    - np.sum(special.gammaln(conc1) - special.gammaln(conc2), -1)
    + np.sum((conc1 - conc2) * (special.digamma(conc1) - special.digamma(
        np.sum(conc1, -1, keepdims=True))), -1))

self.assertAllClose(kl_expected, kl_actual_val, atol=0., rtol=1e-6)
self.assertAllClose(kl_sample_val, kl_actual_val, atol=0., rtol=1e-1)

# Make sure KL(d1||d1) is 0
kl_same = self.evaluate(kullback_leibler.kl_divergence(d1, d1))
self.assertAllClose(kl_same, np.zeros_like(kl_expected))
