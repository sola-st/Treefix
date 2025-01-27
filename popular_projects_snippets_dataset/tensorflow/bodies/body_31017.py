# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
self.assertAllClose(
    np.array([[-0.09, 0.7, -0.05, 0.3, -0.01],
              [0.1, -0.03, 0.5, -0.07, 0.9]]),
    self._npLeakyRelu(
        np.array([[-0.9, 0.7, -0.5, 0.3, -0.1], [0.1, -0.3, 0.5, -0.7,
                                                 0.9]]),
        alpha=0.1))
