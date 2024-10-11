# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
self.assertAllClose(
    np.array([[-1.0433095, 0.73549069, -0.6917582, 0.3152103, -0.16730527],
              [0.1050701, -0.45566732, 0.5253505, -0.88505305, 0.9456309]]),
    self._npSelu(
        np.array([[-0.9, 0.7, -0.5, 0.3, -0.1], [0.1, -0.3, 0.5, -0.7,
                                                 0.9]])))
