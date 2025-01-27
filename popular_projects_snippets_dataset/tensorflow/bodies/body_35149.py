# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
alpha0 = np.array([3.])
beta0 = np.array([1., 2., 3., 1.5, 2.5, 3.5])

alpha1 = np.array([0.4])
beta1 = np.array([0.5, 1., 1.5, 2., 2.5, 3.])

# Build graph.
g0 = gamma_lib.Gamma(concentration=alpha0, rate=beta0)
g1 = gamma_lib.Gamma(concentration=alpha1, rate=beta1)
x = g0.sample(int(1e4), seed=0)
kl_sample = math_ops.reduce_mean(g0.log_prob(x) - g1.log_prob(x), 0)
kl_actual = kullback_leibler.kl_divergence(g0, g1)

# Execute graph.
[kl_sample_, kl_actual_] = self.evaluate([kl_sample, kl_actual])

self.assertEqual(beta0.shape, kl_actual.get_shape())

if not special:
    exit()
kl_expected = ((alpha0 - alpha1) * special.digamma(alpha0)
               + special.gammaln(alpha1)
               - special.gammaln(alpha0)
               + alpha1 * np.log(beta0)
               - alpha1 * np.log(beta1)
               + alpha0 * (beta1 / beta0 - 1.))

self.assertAllClose(kl_expected, kl_actual_, atol=0., rtol=1e-6)
self.assertAllClose(kl_sample_, kl_actual_, atol=0., rtol=1e-1)
