# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
for shape in [(10,), (4, 5)]:
    a1 = 6.0 * np.random.random(size=shape) + 1e-4
    b1 = 6.0 * np.random.random(size=shape) + 1e-4
    a2 = 6.0 * np.random.random(size=shape) + 1e-4
    b2 = 6.0 * np.random.random(size=shape) + 1e-4
    # Take inverse softplus of values to test BetaWithSoftplusConcentration
    a1_sp = np.log(np.exp(a1) - 1.0)
    b1_sp = np.log(np.exp(b1) - 1.0)
    a2_sp = np.log(np.exp(a2) - 1.0)
    b2_sp = np.log(np.exp(b2) - 1.0)

    d1 = beta_lib.Beta(concentration1=a1, concentration0=b1)
    d2 = beta_lib.Beta(concentration1=a2, concentration0=b2)
    d1_sp = beta_lib.BetaWithSoftplusConcentration(concentration1=a1_sp,
                                                   concentration0=b1_sp)
    d2_sp = beta_lib.BetaWithSoftplusConcentration(concentration1=a2_sp,
                                                   concentration0=b2_sp)

    if not special:
        exit()
    kl_expected = (special.betaln(a2, b2) - special.betaln(a1, b1) +
                   (a1 - a2) * special.digamma(a1) +
                   (b1 - b2) * special.digamma(b1) +
                   (a2 - a1 + b2 - b1) * special.digamma(a1 + b1))

    for dist1 in [d1, d1_sp]:
        for dist2 in [d2, d2_sp]:
            kl = kullback_leibler.kl_divergence(dist1, dist2)
            kl_val = self.evaluate(kl)
            self.assertEqual(kl.get_shape(), shape)
            self.assertAllClose(kl_val, kl_expected)

      # Make sure KL(d1||d1) is 0
    kl_same = self.evaluate(kullback_leibler.kl_divergence(d1, d1))
    self.assertAllClose(kl_same, np.zeros_like(kl_expected))
