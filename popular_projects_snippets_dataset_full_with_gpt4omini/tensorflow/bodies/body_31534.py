# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
self.assertAllClose(
    np.array([[11, 22, 33], [41, 52, 63]]),
    self._npBias(
        np.array([[10, 20, 30], [40, 50, 60]]), np.array([1, 2, 3])))
