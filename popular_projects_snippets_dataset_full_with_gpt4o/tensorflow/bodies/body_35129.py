# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
# When concentration = 1, we have an exponential distribution. Check that at
# 0 we have finite log prob.
rate = np.array([0.1, 0.5, 1., 2., 5., 10.], dtype=np.float32)
gamma = gamma_lib.Gamma(concentration=1., rate=rate)
log_pdf = gamma.log_prob(0.)
self.assertAllClose(np.log(rate), self.evaluate(log_pdf))
