# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/betainc_op_test.py
a_s = np.abs(np.random.randn(10, 10) * 1e-16)  # in (0, infty)
b_s = np.abs(np.random.randn(10, 10) * 1e-16)  # in (0, infty)
x_s = np.random.rand(10, 10)  # in (0, 1)
self._testBetaInc(a_s, b_s, x_s, dtypes.float64)
