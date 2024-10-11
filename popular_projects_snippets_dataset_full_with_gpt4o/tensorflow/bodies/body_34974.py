# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/exponential_test.py
batch_size = 7
lam = constant_op.constant([2.0] * batch_size)
lam_v = 2.0
x = np.array([2.5, 2.5, 4.0, 0.1, 1.0, 2.0, 10.0], dtype=np.float32)

exponential = exponential_lib.Exponential(rate=lam)

log_survival = exponential.log_survival_function(x)
self.assertEqual(log_survival.get_shape(), (7,))

if not stats:
    exit()
expected_log_survival = stats.expon.logsf(x, scale=1 / lam_v)
self.assertAllClose(self.evaluate(log_survival), expected_log_survival)
