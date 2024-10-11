# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/exponential_test.py
# Check that Log PDF is finite at 0.
rate = np.array([0.1, 0.5, 1., 2., 5., 10.], dtype=np.float32)
exponential = exponential_lib.Exponential(rate=rate)
log_pdf = exponential.log_prob(0.)
self.assertAllClose(np.log(rate), self.evaluate(log_pdf))
