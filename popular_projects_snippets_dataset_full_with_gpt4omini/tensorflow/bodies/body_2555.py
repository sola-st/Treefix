# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Mul(
    ops.Constant(c, np.array([2.5, 3.3, -1.2, 0.7], dtype)),
    ops.Constant(c, np.array([-1.2, 2, -2, -3], dtype)))
self._ExecuteAndCompareClose(
    c, expected=[[-3, 6.6, 2.4, -2.1]], rtol=3e-3)
